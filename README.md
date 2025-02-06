# Vyper Polygon/Tesseract Workshop

Source code for the agent used for the workshop. 
The agent parses headlines from news sources to find memecoin-worthy content. It then creates a memecoin for the content that it finds, using a Vyper contract to deploy an ERC20 token contract and depositing liquidity for the token into Quickswap. The agent then advertises the newly deployed token on social media.

<p align="center">

<img src="https://github.com/user-attachments/assets/94b34c12-a51c-4954-9f02-72635355de8f"/>

 
</p>


## Setting up your dev environment

1. Install [uv](https://github.com/astral-sh/uv): `pip install uv`
3. Clone this repository and cd into it: `git clone git@github.com:benber86/vyper_tesseract_workshop.git && cd vyper_tesseract_workshop`
4. Set up a virtual environment: `uv venv`
5. Activate the virtual environment: `source .venv/bin/activate`
6. Install the Python dependencies: `uv pip install .`
7. Install the [moccasin](https://github.com/Cyfrin/moccasin) dependencies: `uv run moccasin install`
8. Set up your `.env` file and fill in the values based on the provided `example.env` file

Workshop steps:

- Setting up an environment: Python, uv, moccasin
- Making & deploying an ERC20 token with modules (snekmate)
- Making a factory contract with Blueprints (TokenFactory)
- Making a memecoin factory contract with Quickswap liquidity pools
- Writing tests
- Putting it all together: Using OpenAI's API and functions to make an agent

Ideas to implement for small contest:

- Make the amount of liquidity deployed dynamic based on how strong the agent thinks the meme's potential is
- Use another source instead of news like Solana memecoin deployments
- Do NFTs instead of ERC20
- Add interactivity to the agent: people send ETH and ask on Twitter with a signature to prove ownership
