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

## Workshop steps:

1. **Environment Setup**: Install and configure Python, uv package manager, and Moccasin framework for Vyper development - [Video](https://www.youtube.com/watch?v=DpmQulxFRkg)
2. **Basic ERC20 Token**: Create and deploy a simple ERC20 token using Snekmate modules and Vyper - [Video](https://www.youtube.com/watch?v=yY_XbaQWlk8)
3. **Blueprint Factory**: Build a token factory contract using Vyper's Blueprint pattern for efficient deployment - [Video](https://www.youtube.com/watch?v=V3ahAiedaFM)
4. **Liquidity Integration**: Extend our factory to automatically create Quickswap liquidity pools for new tokens - [Video](https://youtu.be/0zabpBw6OaY)
5. **AI Integration**: Develop an autonomous agent using OpenAI's function calling to generate and deploy memecoins - [Video](https://youtu.be/PGtAkdcG120)
6. **Live Deployment**: Run our complete system live, watching it monitor news, create tokens, and manage social media - [Video](https://youtu.be/RqVcbTX_GXo)

## Running tests

`uv run moccasin test --network polygon-fork`

## Deploying the Token Deployer Contract

`uv run moccasin deploy --network polygon`

## Running the Agent

`uv run mocassin run agent --network polygon`

# Ideas for the Project Contest

Try implementing one or more of these features based on the sample project

1. **Alternative Inputs**: Replace RSS feeds with on-chain event monitoring or real time market data
2. **NFT Variant**: Adapt system for NFT collections instead of ERC20 tokens, taking advantage of AI image generation
3. **Dynamic Liquidity**: Scale initial liquidity amount based on AI-scored meme potential
4. **Agent Interactions**: Create another agent to interact with or comment on the actions of the memecoin agent

Or just roll out your own ideas from scractch!
