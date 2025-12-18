# app.py
# =====================================================
# Essay yig‘uvchi bot
# Livegram-style relay + permissions + album
# =====================================================

import logging
from aiogram import Bot, Dispatcher, executor, types

from config import BOT_TOKEN, ADMIN_ID
from relay import relay_user_to_admin, relay_admin_to_user
from album_handler import handle_album
from permissions import is_user_allowed
from messages import (
    MSG_WELCOME_ALLOWED,
    MSG_NOT_ALLOWED,
)

# -----------------------------------------------------
# Logging
# -----------------------------------------------------
logging.basicConfig(level=logging.INFO)

# -----------------------------------------------------
# Bot init
# -----------------------------------------------------
bot = Bot(token=BOT_TOKEN, parse_mode="Markdown")
dp = Dispatcher(bot)

# =====================================================
# /start COMMAND
# =====================================================
@dp.message_handler(commands=["start"], chat_type=types.ChatType.PRIVATE)
async def start_handler(message: types.Message):
    user_id = message.from_user.id

    # Admin har doim ruxsatli
    if user_id == ADMIN_ID:
        await message.answer(MSG_WELCOME_ALLOWED)
        return

    # Guruh a’zoligini tekshiramiz
    allowed = await is_user_allowed(bot, user_id)

    if allowed:
        await message.answer(MSG_WELCOME_ALLOWED)
    else:
        await message.answer(MSG_NOT_ALLOWED)


# =====================================================
# USER → BOT (PRIVATE CHAT)
# =====================================================
@dp.message_handler(lambda m: m.chat.type == "private" and m.from_user.id != ADMIN_ID)
async def handle_user_message(message: types.Message):
    """
    Foydalanuvchidan kelgan barcha xabarlar:
    - albom bo‘lsa → albom handler
    - bo‘lmasa → relay
    """

    # Albom (media group)
    if message.media_group_id:
        await handle_album(bot, message)
        return

    # Oddiy xabar / rasm / fayl
    await relay_user_to_admin(bot, message)


# =====================================================
# ADMIN → USER (reply orqali)
# =====================================================
@dp.message_handler(
    lambda m: m.chat.type == "private"
    and m.from_user.id == ADMIN_ID
    and m.reply_to_message
)
async def handle_admin_reply(message: types.Message):
    await relay_admin_to_user(bot, message)


# =====================================================
# START BOT
# =====================================================
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
