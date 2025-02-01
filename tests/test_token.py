def test_token_deployment(token):
    assert token.name() == "My MemeCoin"
    assert token.symbol() == "MEME"
