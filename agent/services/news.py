import feedparser
import logging

logger = logging.getLogger(__name__)


class NewsService:
    def __init__(self, feed_url: str):
        self.feed_url = feed_url
        self.processed_ids = set()

    def poll_feed(self) -> list[str]:
        try:
            feed = feedparser.parse(self.feed_url)
            new_items = []
            if not feed.entries:
                logger.error("No news items found in the feed")
                return []

            for entry in feed.entries:
                if entry.id in self.processed_ids:
                    continue

                try:
                    logger.info(f"New headline: {entry.title}")
                    self.processed_ids.add(entry.id)
                    new_items.append(entry.title)
                except Exception as e:
                    logger.error(f"Error parsing entry: {str(e)}")
                    continue

            return new_items

        except Exception as e:
            logger.error(f"Error polling news feed: {str(e)}")
            return []
