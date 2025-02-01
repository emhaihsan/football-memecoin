# pragma version 0.4.0
# @license MIT

from snekmate.auth import ownable
from snekmate.tokens import erc20

initializes: ownable
initializes: erc20[ownable := ownable]
exports: (
    erc20.owner,
    erc20.IERC20,
    erc20.IERC20Detailed,
    erc20.mint,
    erc20.set_minter,
)


@deploy
def __init__():
    ownable.__init__()
    erc20.__init__("My MemeCoin", "MEME", 18, "My MemeCoin", "1")
