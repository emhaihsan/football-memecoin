# pragma version 0.4.0
# @license MIT

# Import the Ownable contract functionality
from snekmate.auth import ownable
# Import the ERC20 token functionality
from snekmate.tokens import erc20

# Initialize the Ownable contract
initializes: ownable
# Initialize the ERC20 contract with the Ownable contract as a dependency
initializes: erc20[ownable := ownable]

# Export specific functionalities from ERC20 and Ownable
exports: (
    erc20.owner,               # Export the owner functionality from ERC20
    erc20.IERC20,              # Export the standard ERC20 interface
    erc20.IERC20Detailed,      # Export the detailed ERC20 interface
    erc20.mint,                # Export the mint functionality
    erc20.set_minter,          # Export the set_minter functionality
    ownable.renounce_ownership,# Export the renounce_ownership functionality
    ownable.transfer_ownership,# Export the transfer_ownership functionality
)

# Constructor for initializing Ownable and ERC20 contracts
@deploy
def __init__(
    name: String[25],       # Token name
    symbol: String[5],      # Token symbol
    decimals: uint8,        # Token decimals
    name_eip712: String[50],# Signing domain's name
    version_eip712: String[20], # Version of the signing domain
):
    ownable.__init__()  # Initialize the Ownable contract
    # Initialize the ERC20 contract with the provided metadata
    erc20.__init__(name, symbol, decimals, name_eip712, version_eip712)
