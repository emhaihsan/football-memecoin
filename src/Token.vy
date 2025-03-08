# pragma version 0.4.0
# @license MIT

from snekmate.auth import ownable  # Import the Ownable contract functionality
from snekmate.tokens import erc20  # Import the ERC20 token functionality

# Initialize the Ownable contract
initializes: ownable

# Initialize the ERC20 contract with the Ownable contract as a dependency
initializes: erc20[ownable := ownable]

# Export specific ERC20 functionalities
exports: (
    erc20.owner,           # Export the owner functionality
    erc20.IERC20,          # Export the standard ERC20 interface
    erc20.IERC20Detailed,  # Export the detailed ERC20 interface
    erc20.mint,            # Export the mint functionality
    erc20.set_minter,      # Export the set_minter functionality
)

# Constructor if in solidity
@deploy
def __init__():
    ownable.__init__()  # Initialize the Ownable contract
    # Initialize the ERC20 token with name, symbol, decimals, and additional details
    erc20.__init__("My MemeCoin", "MEME", 18, "My MemeCoin", "1")
