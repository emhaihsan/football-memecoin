# FootCoin: Football-Themed Memecoin Generator

Source code for an autonomous agent that creates football-themed memecoins.
The agent parses headlines from football news sources to find memecoin-worthy content related to the beautiful game. It then creates a memecoin for the content that it finds, using a Vyper contract to deploy an ERC20 token contract and depositing liquidity for the token into Quickswap. The agent then advertises the newly deployed football-themed token on social media.

<p align="center">

<img src="https://github.com/user-attachments/assets/94b34c12-a51c-4954-9f02-72635355de8f"/>

</p>

## What Makes FootCoin Special?

FootCoin focuses exclusively on football/soccer news (not American football), creating memecoins that resonate with the global football community. The system:

- Monitors football news from reliable sources like BBC Sport
- Evaluates headlines for their memecoin potential based on player popularity, match results, transfers, and more
- Creates football-themed token names, tickers, and promotional content
- Generates football-themed meme images that combine crypto elements with football culture
- Avoids sensitive topics like injuries, politics, and controversial decisions

## Setting up your dev environment

1. Install [uv](https://github.com/astral-sh/uv): `pip install uv`
2. Clone this repository and cd into it: `git clone git@github.com:benber86/vyper_tesseract_workshop.git && cd vyper_tesseract_workshop`
3. Set up a virtual environment: `uv venv`
4. Activate the virtual environment: `source .venv/bin/activate`
5. Install the Python dependencies: `uv pip install .`
6. Install the [moccasin](https://github.com/Cyfrin/moccasin) dependencies: `uv run moccasin install`
7. Set up your `.env` file and fill in the values based on the provided `example.env` file

## How It Works

1. **News Monitoring**: The agent fetches the latest football news from BBC Sport's RSS feed
2. **AI Evaluation**: OpenAI's GPT models evaluate headlines for their memecoin potential
3. **Token Creation**: For worthy headlines, the agent creates a football-themed token name and ticker
4. **Smart Contract Deployment**: A Vyper contract is deployed to create the ERC20 token
5. **Liquidity Provision**: Automatic liquidity is added to Quickswap for trading
6. **Social Media Promotion**: The agent creates and posts promotional content on Twitter

## Running tests

`uv run moccasin test --network polygon-fork`

## Deploying the Token Deployer Contract

`uv run moccasin deploy --network polygon`

## Running the Agent

`uv run moccasin run agent --network polygon`

## Future Enhancements

1. **Team-Specific Feeds**: Add support for team-specific news sources and fan blogs
2. **Tournament Mode**: Special functionality during major tournaments (World Cup, Euros, Champions League)
3. **Player Stats Integration**: Incorporate real-time player statistics to influence token generation
4. **Fan Engagement**: Allow fans to vote on which football news should become memecoins
5. **Multi-Language Support**: Expand to football news in multiple languages to capture global fan bases

## Credits and Acknowledgements

This project is an adaptation of the original codebase from the Vyper/Tesseract Workshop created by [benber86](https://github.com/benber86). The original workshop materials and code can be found at [https://github.com/benber86/vyper_tesseract_workshop/tree/main](https://github.com/benber86/vyper_tesseract_workshop/tree/main).

I've modified the original codebase to focus specifically on football/soccer news and memecoins, while maintaining the core architecture and deployment mechanisms. Special thanks to the workshop creators for providing such an excellent foundation to build upon.

## Disclaimer

This project is for educational and entertainment purposes only. Always do your own research before investing in any cryptocurrency, especially memecoins.
