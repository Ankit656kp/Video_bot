from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "VideoFetchBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Handlers import
import handlers.start
import handlers.video
import handlers.admin

print("🤖 Bot is running...")

app.run()