from src import TokenBlueprint, TokenDeployer, Token
from moccasin.boa_tools import VyperContract
from moccasin.config import get_active_network


def deploy_token_only() -> VyperContract:
    return Token.deploy()

def deploy() -> VyperContract:
    token_blueprint = TokenBlueprint.deploy_as_blueprint()
    token_deployer = TokenDeployer.deploy(token_blueprint)
    result = get_active_network().moccasin_verify(token_deployer)
    result.wait_for_verification()
    return token_deployer


def moccasin_main() -> VyperContract:
    return deploy_token_only()
