# album_handler.py
# =====================================================
# Album (media group) handler
# =====================================================

import asyncio
from collections import defaultdict
from aiogram import Bot, types

from config import ADMIN_ID
from messages import MSG_ESSE_ACCEPTED, MSG_ERROR


# media_group_id → list of messages
albums_buffer = defaultdict(list)


async def handle_album(bot: Bot, message: types.Message):
    """
    Albomdan kelgan rasmlarni yig‘adi va
    to‘liq bo‘lgach admin ga ALBOM holatda forward qiladi
    """

    media_group_id = message.media_group_id

    # 1️⃣ Albomga qo‘shamiz
    albums_buffer[media_group_id].append(message)

    # 2️⃣ Albom tugashini kutamiz
    await asyncio.sleep(2)

    # 3️⃣ Agar bu albom allaqachon yuborilgan bo‘lsa → chiqib ketamiz
    if media_group_id not in albums_buffer:
        return

    album_messages = albums_buffer.pop(media_group_id)

    try:
        # 4️⃣ Albomni admin ga forward qilamiz
        for msg in album_messages:
            await bot.forward_message(
                chat_id=ADMIN_ID,
                from_chat_id=msg.chat.id,
                message_id=msg.message_id
            )

        # 5️⃣ Foydalanuvchiga YAGONA javob
        await message.answer(MSG_ESSE_ACCEPTED)

    except Exception:
        await message.answer(MSG_ERROR)
