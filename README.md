
# Music Bot 🎧

## Overview
This project is a Music Production Chatbot powered by OpenAI's GPT-3.5-turbo. The bot is designed to assist users with music production topics such as mixing, mastering, DAWs, sound design, and music theory. It can be used via a command-line interface (CLI) or integrated with Telegram.

## Features
- **Command-line Chatbot**: Interact with the bot through a CLI to ask music production questions.
- **Telegram Bot Integration**: Use the bot directly in Telegram for real-time assistance.
- **Powered by OpenAI**: Utilizes GPT-3.5-turbo for high-quality and context-aware responses.

## Installation
### Prerequisites
- Python 3.10 or higher
- Pipenv for dependency management

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/dalthuey/music_bot.git
   cd music_bot
   ```

2. Install dependencies:
   ```bash
   pipenv install
   ```

3. Create a `.env` file:
   ```plaintext
   OPENAI_API_KEY=<Your OpenAI API Key>
   TELEGRAM_TOKEN=<Your Telegram Bot Token>
   ```

4. Generate `requirements.txt` (if needed):
   ```bash
   pipenv requirements > requirements.txt
   ```

## Usage
### CLI Mode
1. Run the chatbot in CLI mode:
   ```bash
   python music_production_chatbot.py
   ```
2. Select `1` for CLI interaction.

### Telegram Mode
1. Run the chatbot in Telegram mode:
   ```bash
   python music_production_chatbot.py
   ```
2. Select `2` and interact with the bot via Telegram.

## File Structure
```
music_bot/
├── LICENSE                # Project license
├── Pipfile                # Pipenv dependencies
├── Pipfile.lock           # Locked dependencies
├── README.md              # Project documentation
├── .env.example           # Example environment variables
├── requirements.txt       # Dependencies for pip environments
├── music_production_chatbot.py  # Main script for the chatbot
├── utils.py               # OpenAI Chatbot implementation
```

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing
Feel free to submit issues or pull requests to improve the chatbot!

## Acknowledgements
- [OpenAI](https://openai.com)
- [Python Telegram Bot Library](https://python-telegram-bot.org)
