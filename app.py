# app.py
# =====================================================
# Livegram-style relay bot (base)
# =====================================================

import logging
from aiogram import Bot, Dispatcher, executor, types

from config import BOT_TOKEN, ADMIN_ID
from messages import (
    MSG_WELCOME_ALLOWED,
    MSG_ESSE_ACCEPTED,
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
# USER → ADMIN
# =====================================================
@dp.message_handler(lambda m: m.chat.type == "private" and m.from_user.id != ADMIN_ID)
async def user_to_admin(message: types.Message):
    """
    Foydalanuvchidan kelgan HAR QANDAY xabar
    admin (siz)ga forward qilinadi
    """

    try:
        # 1️⃣ Admin ga yuboramiz
        await bot.forward_message(
            chat_id=ADMIN_ID,
            from_chat_id=message.chat.id,
            message_id=message.message_id
        )

        # 2️⃣ Foydalanuvchiga avtomatik javob
        await message.answer(MSG_ESSE_ACCEPTED)

    except Exception as e:
        await message.answer("❌ Xabarni yuborishda xatolik yuz berdi.")


# =====================================================
# ADMIN → USER (reply orqali)
# =====================================================
@dp.message_handler(
    lambda m: m.chat.type == "private"
    and m.from_user.id == ADMIN_ID
    and m.reply_to_message
)
async def admin_to_user(message: types.Message):
    """
    Admin (siz) forwarded xabarga REPLY qilsa,
    javob o‘sha foydalanuvchiga boradi
    """

    try:
        # Forward qilingan xabarning egasi
        original_user = message.reply_to_message.forward_from

        if not original_user:
            await message.answer("❗️Bu xabarga javob yuborib bo‘lmaydi.")
            return

        await bot.send_message(
            chat_id=original_user.id,
            text=message.text
        )

    except Exception:
        await message.answer("❌ Javob yuborishda xatolik bo‘ldi.")


# =====================================================
# START
# =====================================================
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
