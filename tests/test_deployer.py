import boa
import pytest
from decimal import Decimal

ZERO_ADDRESS = "0x0000000000000000000000000000000000000000"


def test_deploy_new_token(
    token_deployer, token_blueprint, default_account, total_supply, quickswap_factory
):
    new_token, lp_received = token_deployer.deploy_token(
        "SNEK",
        "SNK",
        18,
        "SNEK",
        "1",
        total_supply,
        1_000,
        False,
        value=int(Decimal(1e18)),
    )
    new_token_contract = token_blueprint.at(new_token)
    assert new_token_contract.name() == "SNEK"
    assert new_token_contract.symbol() == "SNK"
    assert new_token_contract.decimals() == 18
    assert new_token_contract.totalSupply() == total_supply
    assert new_token_contract.balanceOf(default_account) == pytest.approx(
        total_supply * 0.1, 1e-6
    )
    assert new_token_contract.owner() == default_account.address

    # Next check from the factory that the pool has been deployed
    pool = quickswap_factory.getPair(
        new_token_contract.address, "0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270"
    )  # wrapped POL address
    assert pool != ZERO_ADDRESS

    # Check that the user has received LP tokens
    assert token_blueprint.at(pool).balanceOf(default_account) > 0


def test_deploy_burn_owner(token_deployer, token_blueprint, total_supply):
    new_token, _ = token_deployer.deploy_token(
        "SNEK",
        "SNK",
        18,
        "SNEK",
        "1",
        total_supply,
        1_000,
        True,
        value=int(Decimal(1e18)),
    )
    new_token_contract = token_blueprint.at(new_token)
    assert new_token_contract.owner() == ZERO_ADDRESS


def test_deploy_revert_no_eth(token_deployer, token_blueprint, total_supply):
    with boa.reverts("ETH amount must be greater than 0"):
        token_deployer.deploy_token(
            "SNEK", "SNK", 18, "SNEK", "1", total_supply, 1_000, False
        )


def test_deploy_revert_no_supply(token_deployer, token_blueprint):
    with boa.reverts("Total supply must be greater than 0"):
        token_deployer.deploy_token(
            "SNEK", "SNK", 18, "SNEK", "1", 0, 1_000, False,
            value=int(Decimal(1e18)),
        )


def test_deploy_revert_excess_owner_share(
    token_deployer, token_blueprint, total_supply
):
    with boa.reverts("Owner share must be lower than 90%"):
        token_deployer.deploy_token(
            "SNEK",
            "SNK",
            18,
            "SNEK",
            "1",
            total_supply,
            9_999,
            False,
            value=int(Decimal(1e18)),
        )
