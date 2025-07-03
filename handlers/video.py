import random
import asyncio
from pyrogram import filters
from pyrogram.types import CallbackQuery
from main import app
from helpers.database import load_sources


@app.on_callback_query(filters.regex("next_video"))
async def send_random_video(client, callback_query: CallbackQuery):
    await callback_query.answer("⏳ Please wait 3 seconds...", show_alert=False)
    await asyncio.sleep(3)

    sources = load_sources()
    if not sources:
        return await callback_query.message.edit_text("❌ No source groups available. Contact admin.")

    random.shuffle(sources)
    for chat_id in sources:
        try:
            async for msg in app.get_chat_history(chat_id, limit=50):
                if msg.video:
                    await callback_query.message.reply_video(
                        msg.video.file_id,
                        caption="🎬 Here's your random video!"
                    )
                    return
        except Exception as e:
            print(f"Error fetching from {chat_id}:", e)

    await callback_query.message.edit_text("⚠️ Could not fetch any videos at the moment. Try again later.")