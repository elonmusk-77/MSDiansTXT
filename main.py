
from pyrogram import Client
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Initialize the bot
app = Client("extractor_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message()
async def handle_message(client, message):
    if message.text.lower() == '/start':
        await message.reply("Welcome to the extractor bot! Please send the API link.")

    # Add other logic as per the functionality
    # such as handling the API link, login credentials, batch selection, etc.

# Run the bot
app.run()
