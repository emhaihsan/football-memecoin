import os
from dotenv import load_dotenv
from pathlib import Path


root_dir = Path(__file__).parent.parent
load_dotenv(root_dir / ".env")


def get_required_env_var(var_name):
    var = os.getenv(var_name)
    if not var:
        raise ValueError(f"{var_name} must be set in .env file")
    return var


FEED_URL = os.getenv("FEED_URL", "https://feeds.nbcnews.com/nbcnews/public/news")
OPENAI_API_KEY = get_required_env_var("OPENAI_API_KEY")
TWITTER_USERNAME = get_required_env_var("TWITTER_USERNAME")
TWITTER_PASSWORD = get_required_env_var("TWITTER_PASSWORD")
TWITTER_EMAIL = get_required_env_var("TWITTER_EMAIL")
WALLET_PRIVATE_KEY = get_required_env_var("WALLET_PRIVATE_KEY")
