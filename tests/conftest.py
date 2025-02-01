from decimal import Decimal

import pytest
import moccasin
from src import TokenBlueprint, TokenFactory, Token, TokenDeployer
from moccasin.boa_tools import VyperContract
from moccasin.config import get_config
from moccasin.moccasin_account import MoccasinAccount


@pytest.fixture
def token() -> VyperContract:
    return Token.deploy()


@pytest.fixture
def token_blueprint() -> VyperContract:
    return TokenBlueprint.deploy_as_blueprint()


@pytest.fixture
def token_factory(token_blueprint) -> VyperContract:
    return TokenFactory.deploy(token_blueprint)


@pytest.fixture
def token_deployer(token_blueprint) -> VyperContract:
    return TokenDeployer.deploy(token_blueprint)


@pytest.fixture
def quickswap_factory() -> VyperContract:
    factory = get_config().get_active_network().manifest_named("quickswap_factory")
    return factory


@pytest.fixture
def default_account() -> MoccasinAccount:
    return moccasin.config.get_active_network().get_default_account()


@pytest.fixture
def total_supply() -> int:
    return int(500_000 * Decimal(1e18))
