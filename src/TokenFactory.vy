# pragma version 0.4.0
# @license MIT
ERC20_IMPL: public(immutable(address))


@deploy
def __init__(erc20_impl: address):
    ERC20_IMPL = erc20_impl


@external
def deploy_token(
    name: String[25],
    symbol: String[5],
    decimals: uint8,
    name_eip712: String[50],
    version_eip712: String[20],
) -> address:
    new_token: address = create_from_blueprint(
        ERC20_IMPL, name, symbol, decimals, name_eip712, version_eip712
    )
    return new_token
