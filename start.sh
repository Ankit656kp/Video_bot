from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from main import app
from config import OWNER_ID, FORCE_JOIN
from helpers.database import save_user
from helpers.force_join import check_force_join


@app.on_message(filters.command("start") & filters.private)
async def start_command(client, message: Message):
    user = message.from_user
    save_user({
        "id": user.id,
        "username": user.username or "",
        "first_name": user.first_name or ""
    })

    joined = await check_force_join(client, message)
    if not joined:
        btn = InlineKeyboardMarkup(
            [[InlineKeyboardButton("📢 Join Channel", url=FORCE_JOIN)]]
        )
        return await message.reply(
            "**🚫 Please join our channel to use the bot.**",
            reply_markup=btn
        )

    buttons = InlineKeyboardMarkup(
        [[InlineKeyboardButton("📽 Next Video", callback_data="next_video")]]
    )
    await message.reply(
        f"👋 Hello {user.first_name}!\n\nClick below to watch a random video.",
        reply_markup=buttons
    )