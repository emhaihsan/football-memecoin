import logging
from decimal import Decimal

from web3 import Web3
from eth_account import Account
import random

logger = logging.getLogger(__name__)


class DeployerService:
    def __init__(self, private_key: str):
        self.w3 = Web3(Web3.HTTPProvider("https://polygon-rpc.com"))
        self.account = Account.from_key(private_key)
        self.contract_address = "0xa2E4c9dbcC50A66ad9aD56ED2808C2D71b9c9d1e"
        self.contract_abi = [
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
        self.contract = self.w3.eth.contract(
            address=self.contract_address, abi=self.contract_abi
        )

    def deploy_token(self, name: str, symbol: str) -> str | None:
        try:
            decimals = 18
            name_eip712 = name
            version_eip712 = "1"
            total_supply = int(42_690_000 * Decimal(1e18))
            owner_share = random.randint(5, 25)
            burn_owner = True

            gas_estimate = self.contract.functions.deploy_token(
                name,
                symbol,
                decimals,
                name_eip712,
                version_eip712,
                total_supply,
                owner_share,
                burn_owner,
            ).estimate_gas(
                {"from": self.account.address, "value": self.w3.to_wei(0.001, "ether")}
            )

            transaction = self.contract.functions.deploy_token(
                name,
                symbol,
                decimals,
                name_eip712,
                version_eip712,
                total_supply,
                owner_share,
                burn_owner,
            ).build_transaction(
                {
                    "from": self.account.address,
                    "value": self.w3.to_wei(0.001, "ether"),
                    "gas": int(gas_estimate * 1.2),
                    "gasPrice": self.w3.eth.gas_price,
                    "nonce": self.w3.eth.get_transaction_count(self.account.address),
                }
            )

            signed_txn = self.account.sign_transaction(transaction)
            tx_hash = self.w3.eth.send_raw_transaction(signed_txn.raw_transaction)
            tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)

            if tx_receipt["status"] == 1:
                new_token_address = tx_receipt["logs"][1][
                    "address"
                ]  # get the token address from ownership transfer event
                logger.info(f"Token deployed successfully at {new_token_address}")
                return new_token_address
            else:
                logger.error("Token deployment failed")
                return None

        except Exception as e:
            logger.error(f"Error deploying token: {str(e)}")
            return None
