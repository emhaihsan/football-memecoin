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


FEED_URL = os.getenv("FEED_URL", "https://feeds.bbci.co.uk/sport/football/rss.xml")
OPENAI_API_KEY = get_required_env_var("OPEN_AI_KEY")
TWITTER_USERNAME = get_required_env_var("TWITTER_USERNAME")
TWITTER_PASSWORD = get_required_env_var("TWITTER_PASSWORD")
TWITTER_EMAIL = get_required_env_var("TWITTER_EMAIL")
