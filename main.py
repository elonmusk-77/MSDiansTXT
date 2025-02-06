
from pyrogram import Client
from dotenv import load_dotenv
import os
import time
from datetime import datetime, timezone  # Ensure 'timezone' is imported


# Define your bot credentials
API_ID = int(os.getenv("API_ID", "your_api_id"))
API_HASH = os.getenv("API_HASH", "your_api_hash")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")

# Initialize Pyrogram Client
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Force time synchronization
telegram_time_offset = int(time.time()) - int(datetime.now(timezone.utc).timestamp())
if abs(telegram_time_offset) > 1:
    print(f"Adjusting Telegram time offset: {telegram_time_offset}")
    time.sleep(abs(telegram_time_offset))  # Delay to sync time

# Start the bot
if __name__ == "__main__":
    app.run()

@app.on_message()
async def handle_message(client, message):
    if message.text.lower() == '/start':
        await message.reply("Welcome to the extractor bot! Please send the API link.")

    # Add other logic as per the functionality
    # such as handling the API link, login credentials, batch selection, etc.

# Run the bot
app.run()
