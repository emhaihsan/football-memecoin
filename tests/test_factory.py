def test_factory_deployment(token_factory, token_blueprint):
    for i in range(2):
        token_address = token_factory.deploy_token(
            f"Snek{i}", f"SNK{i}", 18, f"Snek{i}", f"{i}"
        )
        print(f"Token deployed at: {token_address}")
        token = token_blueprint.deployer.at(
            token_address
        )  # Newer boa versions will allow token_blueprint.at(token_address)
        assert token.name() == f"Snek{i}"
        assert token.symbol() == f"SNK{i}"
