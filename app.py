# app.py
# =====================================================
# Final entry point: Livegram + permissions + album
# =====================================================

import logging
from aiogram import Bot, Dispatcher, executor, types

from config import BOT_TOKEN, ADMIN_ID
from relay import relay_user_to_admin, relay_admin_to_user
from album_handler import handle_album
from permissions import is_user_allowed

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
# USER → BOT (PRIVATE CHAT)
# =====================================================
@dp.message_handler(lambda m: m.chat.type == "private" and m.from_user.id != ADMIN_ID)
async def handle_user_message(message: types.Message):
    """
    Foydalanuvchidan kelgan barcha xabarlar shu yerga tushadi
    """

    # 1️⃣ Albom bo‘lsa — alohida handler
    if message.media_group_id:
        await handle_album(bot, message)
        return

    # 2️⃣ Albom bo‘lmasa — oddiy relay
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
# START
# =====================================================
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
