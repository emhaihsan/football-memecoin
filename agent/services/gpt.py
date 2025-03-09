import json
from openai import OpenAI
import logging

from agent.model.token import MemeToken

logger = logging.getLogger(__name__)


class AIService:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def evaluate_headlines(self, headlines: list[str]) -> dict[str, bool]:
        try:
            functions = [
                {
                    "name": "evaluate_meme_potential",
                    "description": "Evaluate if news headlines have potential for memecoins",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "evaluations": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "headline": {
                                            "type": "string",
                                            "description": "The news headline",
                                        },
                                        "is_worthy": {
                                            "type": "boolean",
                                            "description": "Whether the headline is worthy of a memecoin",
                                        },
                                        "reasoning": {
                                            "type": "string",
                                            "description": "Explanation of the decision",
                                        },
                                    },
                                    "required": ["headline", "is_worthy", "reasoning"],
                                },
                            }
                        },
                        "required": ["evaluations"],
                    },
                }
            ]

            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": """You are an expert at identifying viral meme potential in news headlines. 
                        A headline is meme-worthy if it involves:
                        - Celebrities doing something controversial or silly
                        - Tech billionaires making headlines
                        - Unusual or absurd situations
                        - Popular culture moments
                        - Viral trends or phenomena
                        Be selective and original - only truly viral-worthy and new content should return true. 
                        We are only looking at launching one single new meme coin every now and then.
                        We don't want to launch a memecoin that already exists like $TRUMP, $MUSK or $BIDEN.
                        Examples of news-based meme coins include:
                        $BODEN about President Joe Biden during the election
                        $TRUMP launched during the 2024 U.S. presidential election
                        $MOODENG based on a baby pygmy hippo living in a zoo in Thailand
                        $LUIGI based on the news that 'the CEO of the largest insurance company in America was shot by digital nomad Luigi Nicholas Mangione'
                        $HARAMBE as a tribute to the beloved gorilla of the same name""",
                    },
                    {
                        "role": "user",
                        "content": f"Evaluate these headlines for meme potential: {json.dumps(headlines)}",
                    },
                ],
                functions=functions,
                function_call={"name": "evaluate_meme_potential"},
            )

            result = json.loads(response.choices[0].message.function_call.arguments)

            return {
                evaluation["headline"]: evaluation["is_worthy"]
                for evaluation in result["evaluations"]
            }

        except Exception as e:
            logger.error(f"Error in batch AI evaluation: {str(e)}")
            return {headline: False for headline in headlines}

    def select_best_meme(self, worthy_headlines: list[str]) -> MemeToken | None:
        try:
            functions = [
                {
                    "name": "select_best_meme",
                    "description": "Select the best headline for a memecoin and generate metadata",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string",
                                "description": "Full name for the memecoin",
                            },
                            "ticker": {
                                "type": "string",
                                "description": "Trading symbol for the coin (2-5 chars)",
                            },
                            "shill_line": {
                                "type": "string",
                                "description": "140 char tweet shilling the coin",
                            },
                            "headline": {
                                "type": "string",
                                "description": "The original headline this is based on",
                            },
                        },
                        "required": ["name", "ticker", "shill_line", "headline"],
                    },
                }
            ]

            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": """You are an expert memecoin creator and crypto marketer.
                        Select the most viral-worthy headline and create a memecoin around it.
                        The ticker should be catchy, relevant and 2-5 chars.
                        The copy should be engaging and include the ticker.
                        Examples:
                        $PEPE - The most memeable frog
                        $TURBO - AI Trading gone wild
                        $WIF - Wife changing money season
                        Make it fun and engaging but not offensive. Make sure that the tagline does not go against the OpenAI image generation safety system as it will be used to genreate an image with DALL-E.""",
                    },
                    {
                        "role": "user",
                        "content": f"Create the best possible memecoin from these headlines: {json.dumps(worthy_headlines)}",
                    },
                ],
                functions=functions,
                function_call={"name": "select_best_meme"},
            )

            result = json.loads(response.choices[0].message.function_call.arguments)
            return MemeToken(**result)

        except Exception as e:
            logger.error(f"Error selecting best meme: {str(e)}")
            return None

    def generate_meme_image(self, token: MemeToken) -> str | None:
        try:
            response = self.client.images.generate(
                model="dall-e-3",
                prompt=f"""Create a crypto meme image for ${token.ticker} token.
                Context: {token.headline}
                The image should be memetic, viral-worthy and related to the headline.
                Style: Combine crypto art elements with meme culture.
                Make it fun and engaging.
                Include the ticker ${token.ticker} prominently in the image.""",
                size="1024x1024",
                quality="standard",
                n=1,
            )

            return response.data[0].url

        except Exception as e:
            logger.error(f"Error generating image: {str(e)}")
            return None
