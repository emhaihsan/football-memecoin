# pragma version 0.4.0
# @license MIT

# Declare an immutable variable for the ERC20 implementation contract address
ERC20_IMPL: public(immutable(address))

# The constructor function initializes the contract with the address of the ERC20 implementation
@deploy
def __init__(erc20_impl: address):
    # Set the ERC20_IMPL to the provided implementation address
    ERC20_IMPL = erc20_impl

# External function to deploy a new token using the blueprint
@external
def deploy_token(
    name: String[25],              # Name of the token
    symbol: String[5],             # Symbol of the token
    decimals: uint8,               # Decimal precision of the token
    name_eip712: String[50],       # EIP712 domain name
    version_eip712: String[20],    # EIP712 domain version
) -> address:
    # Create a new token from the blueprint using the provided parameters
    new_token: address = create_from_blueprint(
        ERC20_IMPL, name, symbol, decimals, name_eip712, version_eip712
    )
    # Return the address of the newly created token
    return new_token
