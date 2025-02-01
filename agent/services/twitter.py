import asyncio
import os
import requests
from twikit import Client
import logging

logger = logging.getLogger(__name__)


class TwitterService:
    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password
        self.client = Client("en-US")
        self.is_logged_in = False

    async def ensure_login(self):
        if not self.is_logged_in:
            try:
                await self.client.login(
                    auth_info_1=self.username,
                    auth_info_2=self.email,
                    password=self.password,
                )
                self.is_logged_in = True
                logger.info("Successfully logged in to Twitter")
            except Exception as e:
                logger.error(f"Failed to login to Twitter: {str(e)}")
                raise

    async def post_meme_async(self, text: str, image_url: str) -> bool:
        try:
            await self.ensure_login()

            temp_image_path = "temp_meme.jpg"
            response = requests.get(image_url)
            response.raise_for_status()

            with open(temp_image_path, "wb") as f:
                f.write(response.content)

            try:
                media_id = await self.client.upload_media(temp_image_path)
                await self.client.create_tweet(text=text, media_ids=[media_id])
                logger.info("Successfully posted meme to Twitter")
                return True

            finally:
                if os.path.exists(temp_image_path):
                    os.remove(temp_image_path)
                    logger.debug("Cleaned up temporary image file")

        except Exception as e:
            logger.error(f"Failed to post meme to Twitter: {str(e)}")
            return False

    def post_meme(self, text: str, image_url: str) -> bool:
        return asyncio.run(self.post_meme_async(text, image_url))
