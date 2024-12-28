import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes
from telegram.ext.filters import TEXT
from utils import OpenAIChatbot
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the OpenAI chatbot
chatbot = OpenAIChatbot()

# Telegram Command Handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handles the /start command and introduces the bot.
    """
    await update.message.reply_text(
        "Hi! I'm your Music Production Chatbot. Ask me anything about music production!"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handles user messages and generates a response using the OpenAIChatbot class.
    """
    user_message = update.message.text
    bot_response = chatbot.get_response(user_message)
    await update.message.reply_text(bot_response)

# Telegram Main Function
def start_telegram_bot():
    """
    Starts the Telegram bot and begins polling for updates.
    """
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    if not TELEGRAM_TOKEN:
        print("Error: Telegram token is missing. Please add it to your .env file.")
        return

    # Initialize Telegram bot application
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Register command and message handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(TEXT, handle_message))

    print("Telegram Bot is running... Press Ctrl+C to stop.")
    app.run_polling()

# CLI Main Function
def start_cli():
    """
    Command-line interface for the Music Production Chatbot.
    """
    print("\n🎧 Welcome to the Music Production Chatbot! 🎶")
    print("Ask me anything about music production, DAWs, mixing, mastering, and more!")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("🎸 Exiting Music Production Chatbot. Keep making great music!")
            break

        response = chatbot.get_response(user_input)
        print(f"\nBot: {response}\n")

# Main Function
if __name__ == "__main__":
    # Get mode from environment variable or default to Telegram
    mode = os.getenv("BOT_MODE", "telegram").lower()

    if mode == "cli":
        print("🎧 Running in CLI mode...")
        start_cli()
    elif mode == "telegram":
        print("🤖 Running in Telegram mode...")
        start_telegram_bot()
    else:
        print(f"Error: Invalid BOT_MODE '{mode}'. Please set BOT_MODE to 'cli' or 'telegram'.")
