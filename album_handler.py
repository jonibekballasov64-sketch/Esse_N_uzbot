# album_handler.py
# =====================================================
# Album (media group) handler — B VARIANT
# ADMIN ga ALBOM-ALBOM qilib yuboradi
# =====================================================

import asyncio
from collections import defaultdict
from aiogram import Bot, types

from config import ADMIN_ID
from messages import MSG_ESSE_ACCEPTED, MSG_ERROR


# media_group_id → list of messages
albums_buffer = defaultdict(list)


async def handle_album(bot: Bot, message: types.Message):
    media_group_id = message.media_group_id

    # 1️⃣ Albomga qo‘shamiz
    albums_buffer[media_group_id].append(message)

    # 2️⃣ Albom tugashini kutamiz
    await asyncio.sleep(2)

    # 3️⃣ Agar bu albom allaqachon yuborilgan bo‘lsa — chiqib ket
    if media_group_id not in albums_buffer:
        return

    album_messages = albums_buffer.pop(media_group_id)

    try:
        media = []

        for idx, msg in enumerate(album_messages):
            # 📸 RASM
            if msg.photo:
                media.append(
                    types.InputMediaPhoto(
                        media=msg.photo[-1].file_id,
                        caption=(
                            f"👤 {msg.from_user.full_name}\n"
                            f"🆔 {msg.from_user.id}"
                            if idx == 0 else None
                        )
                    )
                )

            # 📄 HUJJAT (PDF, WORD)
            elif msg.document:
                media.append(
                    types.InputMediaDocument(
                        media=msg.document.file_id,
                        caption=(
                            f"👤 {msg.from_user.full_name}\n"
                            f"🆔 {msg.from_user.id}"
                            if idx == 0 else None
                        )
                    )
                )

        # 4️⃣ ADMIN GA — HAQIQIY ALBOM
        if media:
            await bot.send_media_group(
                chat_id=ADMIN_ID,
                media=media
            )

        # 5️⃣ Foydalanuvchiga — 1 marta javob
        await message.answer(MSG_ESSE_ACCEPTED)

    except Exception as e:
        print("ALBUM ERROR:", e)
        await message.answer(MSG_ERROR)
