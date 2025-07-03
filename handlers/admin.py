from pyrogram import filters
from pyrogram.types import Message
from main import app
from config import OWNER_ID
from helpers.database import (
    load_users, load_sources,
    add_source, remove_source
)


def is_owner():
    return filters.user(OWNER_ID)


@app.on_message(filters.command("broadcast") & is_owner())
async def broadcast_message(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("❗Reply to a message you want to broadcast.")
    
    users = load_users()
    count = 0
    for user in users:
        try:
            await message.reply_to_message.copy(user["id"])
            count += 1
        except:
            pass
    await message.reply(f"✅ Broadcast sent to {count} users.")


@app.on_message(filters.command("stats") & is_owner())
async def show_stats(client, message: Message):
    users = load_users()
    text = f"👤 Total Users: {len(users)}\n\n"
    for u in users:
        text += f"- {u['first_name']} (@{u['username']}) | `{u['id']}`\n"
    await message.reply(text)


@app.on_message(filters.command("addsource") & is_owner())
async def add_source_cmd(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("❗Usage: /addsource -100xxxxxxxxx")
    group_id = message.command[1]
    add_source(group_id)
    await message.reply(f"✅ Source group `{group_id}` added.")


@app.on_message(filters.command("removesource") & is_owner())
async def remove_source_cmd(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("❗Usage: /removesource -100xxxxxxxxx")
    group_id = message.command[1]
    remove_source(group_id)
    await message.reply(f"✅ Source group `{group_id}` removed.")


@app.on_message(filters.command("sourcegroups") & is_owner())
async def list_sources(client, message: Message):
    sources = load_sources()
    if not sources:
        return await message.reply("📭 No source groups added yet.")
    text = "**📁 Current Source Groups:**\n\n"
    text += "\n".join([f"`{g}`" for g in sources])
    await message.reply(text)
