# permissions.py
# =====================================================
# Foydalanuvchi ruxsatini tekshirish
# =====================================================

from aiogram import Bot
from aiogram.utils.exceptions import ChatNotFound, BotNotMember


async def is_user_allowed(bot: Bot, user_id: int) -> bool:
    """
    Foydalanuvchi bot admin bo‘lgan kamida bitta
    yopiq guruh a’zosi bo‘lsa → TRUE

    Aks holda → FALSE
    """

    try:
        # Bot qaysi guruhlarda admin ekanini Telegram API
        # o‘zi biladi, biz faqat tekshiramiz
        dialogs = await bot.get_my_dialogs()

        for dialog in dialogs:
            chat = dialog.chat

            # Faqat supergroup / group
            if chat.type not in ("group", "supergroup"):
                continue

            try:
                member = await bot.get_chat_member(chat.id, user_id)
                if member.status in ("member", "administrator", "creator"):
                    return True
            except (ChatNotFound, BotNotMember):
                continue

    except Exception:
        pass

    return False
