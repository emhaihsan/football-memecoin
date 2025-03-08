from src import TokenBlueprint, TokenDeployer, Token
from moccasin.boa_tools import VyperContract
from moccasin.config import get_active_network

def deploy_token_only() -> VyperContract:
    print("Deploying Token contract...")
    token = Token.deploy()
    print(f"Token deployed at: {token.address}")
    return token

def deploy() -> VyperContract:
    print("Deploying TokenBlueprint...")
    token_blueprint = TokenBlueprint.deploy_as_blueprint()
    print(f"TokenBlueprint deployed at: {token_blueprint.address}")

    print("Deploying TokenDeployer...")
    token_deployer = TokenDeployer.deploy(token_blueprint)
    print(f"TokenDeployer deployed at: {token_deployer.address}")

    print("Verifying TokenDeployer on the network...")
    result = get_active_network().moccasin_verify(token_deployer)
    result.wait_for_verification()
    print("Verification complete!")
    return token_deployer

def moccasin_main() -> VyperContract:
    print("Starting deployment...")
    return deploy_token_only()