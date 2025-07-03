from pyrogram.types import Message
from pyrogram.errors import UserNotParticipant
from config import FORCE_JOIN
from pyrogram import Client

async def check_force_join(app: Client, message: Message):
    if "t.me/" not in FORCE_JOIN:
        return True  # Force join disabled

    try:
        # Extract channel username from invite link
        if "+" in FORCE_JOIN:
            # Invite link
            invite_link = FORCE_JOIN.split("/")[-1]
            await app.get_chat_member(invite_link, message.from_user.id)
        else:
            # Username link
            channel_username = FORCE_JOIN.split("/")[-1]
            await app.get_chat_member(channel_username, message.from_user.id)
        return True
    except UserNotParticipant:
        return False
    except Exception as e:
        print("Force join error:", e)
        return True  # Fail-safe: allow access if error