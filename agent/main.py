import logging
import time

from agent.config import (
    FEED_URL,
    OPENAI_API_KEY,
    TWITTER_USERNAME,
    TWITTER_PASSWORD,
    TWITTER_EMAIL,
    WALLET_PRIVATE_KEY,
)
from agent.services.deployer import DeployerService
from agent.services.news import NewsService
from agent.services.gpt import AIService
from agent.services.twitter import TwitterService

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


async def post_to_twitter(twitter_service, token, image_url):
    success = await twitter_service.post_meme(
        text=token.shill_line, image_url=image_url
    )
    if success:
        logger.info("Successfully posted to Twitter")
    else:
        logger.error("Failed to post to Twitter")


def main():
    news_service = NewsService(FEED_URL)
    ai_service = AIService(OPENAI_API_KEY)
    deployer_service = DeployerService(WALLET_PRIVATE_KEY)
    twitter_service = TwitterService(TWITTER_USERNAME, TWITTER_EMAIL, TWITTER_PASSWORD)
    while True:
        headlines = news_service.poll_feed()
        if headlines:
            evaluations = ai_service.evaluate_headlines(headlines)
            worthy_headlines = []
            for headline, is_worthy in evaluations.items():
                if is_worthy:
                    logger.info(f"🚀 MEME POTENTIAL DETECTED: {headline}")
                    worthy_headlines.append(headline)

            if worthy_headlines:
                token = ai_service.select_best_meme(worthy_headlines)
                if token:
                    logger.info(f"Selected meme: {token.model_dump_json()}")
                    image_url = ai_service.generate_meme_image(token)
                    if image_url:
                        logger.info(f"Generated meme image: {image_url}")

                        new_token_address = deployer_service.deploy_token(
                            token.name, token.ticker
                        )
                        if new_token_address:
                            quickswap_link = f"https://quickswap.exchange/#/swap?outputCurrency={new_token_address}"
                            tweet_text = f"{token.shill_line}\n\nGet in on QuickSwap: {quickswap_link}"

                            success = twitter_service.post_meme(tweet_text, image_url)
                            if success:
                                logger.info("Successfully posted to Twitter")
                            else:
                                logger.error("Failed to post to Twitter")
                        else:
                            logger.error("Failed to deploy token")
        time.sleep(15 * 60)


if __name__ == "__main__":
    main()
