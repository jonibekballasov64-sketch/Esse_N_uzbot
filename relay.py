# relay.py
# =====================================================
# Lovegram-style relay logic (with permission check)
# =====================================================

from aiogram import Bot, types

from config import ADMIN_ID
from permissions import is_user_allowed
from messages import (
    MSG_WELCOME_ALLOWED,
    MSG_NOT_ALLOWED,
    MSG_ESSE_ACCEPTED,
    MSG_ERROR,
)


# =====================================================
# USER → ADMIN
# =====================================================
async def relay_user_to_admin(bot: Bot, message: types.Message):
    """
    Foydalanuvchidan kelgan xabar:
    - agar ruxsatli bo‘lsa → admin ga yuboriladi
    - bo‘lmasa → rad etiladi
    """

    user_id = message.from_user.id

    # 1️⃣ Ruxsat tekshiruvi
    allowed = await is_user_allowed(bot, user_id)

    if not allowed:
        await message.answer(MSG_NOT_ALLOWED)
        return

    try:
        # 2️⃣ Admin ga yuborish
        await bot.forward_message(
            chat_id=ADMIN_ID,
            from_chat_id=message.chat.id,
            message_id=message.message_id
        )

        # 3️⃣ Foydalanuvchiga javob
        await message.answer(MSG_ESSE_ACCEPTED)

    except Exception:
        await message.answer(MSG_ERROR)


# =====================================================
# ADMIN → USER
# =====================================================
async def relay_admin_to_user(bot: Bot, message: types.Message):
    """
    Admin forwarded xabarga reply qilsa,
    javob o‘sha foydalanuvchiga boradi
    """

    try:
        original = message.reply_to_message.forward_from

        if not original:
            await message.answer("❗️Bu xabarga javob yuborib bo‘lmaydi.")
            return

        await bot.send_message(
            chat_id=original.id,
            text=message.text
        )

    except Exception:
        await message.answer(MSG_ERROR)
