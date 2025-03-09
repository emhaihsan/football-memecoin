import logging
from decimal import Decimal
import random
from moccasin.config import get_config
from moccasin.named_contract import NamedContract

logger = logging.getLogger(__name__)
ABI = [
            {
                "inputs": [
                    {"internalType": "string", "name": "name", "type": "string"},
                    {"internalType": "string", "name": "symbol", "type": "string"},
                    {"internalType": "uint8", "name": "decimals", "type": "uint8"},
                    {"internalType": "string", "name": "name_eip712", "type": "string"},
                    {
                        "internalType": "string",
                        "name": "version_eip712",
                        "type": "string",
                    },
                    {
                        "internalType": "uint256",
                        "name": "total_supply",
                        "type": "uint256",
                    },
                    {
                        "internalType": "uint256",
                        "name": "owner_share",
                        "type": "uint256",
                    },
                    {"internalType": "bool", "name": "burn_owner", "type": "bool"},
                ],
                "name": "deploy_token",
                "outputs": [
                    {"internalType": "address", "name": "", "type": "address"},
                    {"internalType": "uint256", "name": "", "type": "uint256"},
                ],
                "stateMutability": "payable",
                "type": "function",
            }
        ]
def deploy_token(name: str, symbol: str) -> str | None:
    try:
        network = get_config().get_active_network()
        token_factory: NamedContract = network.manifest_named_contract(contract_name="TokenDeployer", force_deploy=False, abi=ABI, address="0xa2E4c9dbcC50A66ad9aD56ED2808C2D71b9c9d1e")

        decimals = 18
        name_eip712 = name
        version_eip712 = "1"
        total_supply = int(42_690_000 * Decimal(1e18))
        owner_share = random.randint(5, 25)
        burn_owner = True

        new_token, _ = token_factory.deploy_token(
            name,
            symbol,
            decimals,
            name_eip712,
            version_eip712,
            total_supply,
            owner_share,
            burn_owner,
            value=int(Decimal(1e17)),
        )
        logger.info(f"New token deployed: {new_token}")
        return new_token

    except Exception as e:
        logger.error(f"Error deploying token: {str(e)}")
        return None