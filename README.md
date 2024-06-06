
# Discord Bot Project

This project is a simple Discord bot that responds to specific messages and commands. It utilizes the `discord` library for interaction with Discord and the `better_profanity` library for filtering inappropriate language.

## Project Structure

The project consists of three main files:
1. `bot.py` - Contains the main bot logic and handles message events.
2. `responses.py` - Defines the responses to specific messages.
3. `main.py` - Entry point for running the bot.

### `bot.py`

This file includes the core functionality of the Discord bot. It sets up the Discord client, listens for messages, and delegates responses to the `responses.py` module.


### `responses.py`

This file handles the logic for responding to specific messages. It includes basic responses and a coin flip command.

### `main.py`

This file serves as the entry point for running the bot.

## Requirements

- Python 3.6 or higher
- `discord.py` library
- `better_profanity` library

## Installation

1. Clone the repository.
2. Install the required libraries:
   ```sh
   pip install discord.py better_profanity
   ```
3. Run `main.py` and enter your bot's token when prompted.

## Usage

- Type `hello` to receive a greeting.
- Type `!dice` to flip a coin.
- Type `!help` for a list of commands.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.
