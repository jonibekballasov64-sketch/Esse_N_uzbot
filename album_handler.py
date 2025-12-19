# album_handler.py
# =====================================================
# Album (media group) handler — ALBOM → ALBOM
# =====================================================

import asyncio
from collections import defaultdict
from aiogram import Bot, types

from config import ADMIN_ID
from messages import MSG_AFTER_SUBMIT, MSG_ERROR


# media_group_id → list of messages
albums_buffer = defaultdict(list)


async def handle_album(bot: Bot, message: types.Message):
    """
    Foydalanuvchidan kelgan albomni yig‘adi
    va admin ga HAM ALBOM HOLIDA yuboradi
    """

    media_group_id = message.media_group_id

    # 1️⃣ Albomga qo‘shamiz
    albums_buffer[media_group_id].append(message)

    # 2️⃣ Albom tugashini kutamiz
    await asyncio.sleep(2)

    # 3️⃣ Agar allaqachon yuborilgan bo‘lsa — chiqib ket
    if media_group_id not in albums_buffer:
        return

    album_messages = albums_buffer.pop(media_group_id)

    try:
        media = []

        for msg in album_messages:
            if msg.photo:
                media.append(
                    types.InputMediaPhoto(
                        media=msg.photo[-1].file_id,
                        caption=(
                            f"👤 {msg.from_user.full_name}\n"
                            f"🆔 {msg.from_user.id}"
                            if not media else None
                        )
                    )
                )
            elif msg.document:
                media.append(
                    types.InputMediaDocument(
                        media=msg.document.file_id
                    )
                )

        # 4️⃣ ADMIN GA ALBOM HOLIDA YUBORAMIZ
        await bot.send_media_group(
            chat_id=ADMIN_ID,
            media=media
        )

        # 5️⃣ Foydalanuvchiga BIR MARTA javob
        await message.answer(MSG_AFTER_SUBMIT)

    except Exception as e:
        print("ALBUM ERROR:", e)
        await message.answer(MSG_ERROR)
