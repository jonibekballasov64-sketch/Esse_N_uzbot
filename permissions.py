# permissions.py
# =====================================================
# Foydalanuvchi ruxsatini tekshirish
# =====================================================

from aiogram import Bot
from aiogram.utils.exceptions import ChatNotFound
from config import ALLOWED_GROUP_IDS


async def is_user_allowed(bot: Bot, user_id: int) -> bool:
    """
    Foydalanuvchi kamida bitta ruxsat berilgan
    yopiq guruh a’zosi bo‘lsa → TRUE
    """

    for group_id in ALLOWED_GROUP_IDS:
        try:
            member = await bot.get_chat_member(group_id, user_id)
            if member.status in ("member", "administrator", "creator"):
                return True
        except ChatNotFound:
            continue
        except Exception:
            continue

    return False
