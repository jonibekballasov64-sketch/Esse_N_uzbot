import logging
from aiogram import Bot, Dispatcher, executor, types

from config import BOT_TOKEN, ADMIN_ID
from relay import relay_user_to_admin, relay_admin_to_user
from album_handler import handle_album
from permissions import is_user_allowed
from messages import MSG_WELCOME_ALLOWED, MSG_NOT_ALLOWED, MSG_AFTER_SUBMIT

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, parse_mode="Markdown")
dp = Dispatcher(bot)


# =====================================================
# /start
# =====================================================
@dp.message_handler(commands=["start"], chat_type=types.ChatType.PRIVATE)
async def start_handler(message: types.Message):
    user_id = message.from_user.id

    if user_id == ADMIN_ID:
        await message.answer(MSG_WELCOME_ALLOWED)
        return

    if await is_user_allowed(bot, user_id):
        await message.answer(MSG_WELCOME_ALLOWED)
    else:
        await message.answer(MSG_NOT_ALLOWED)


# =====================================================
# USER → BOT (HAMMA TURDAGI XABARLAR)
# =====================================================
@dp.message_handler(
    lambda m: m.chat.type == "private" and m.from_user.id != ADMIN_ID,
    content_types=types.ContentTypes.ANY
)
async def handle_user_message(message: types.Message):

    user_id = message.from_user.id

    # Ruxsat tekshiruvi
    if not await is_user_allowed(bot, user_id):
        await message.answer(MSG_NOT_ALLOWED)
        return

    # Albom bo‘lsa
    if message.media_group_id:
        await handle_album(bot, message)
        return

    # Oddiy xabar (rasm / matn / pdf / word)
    await relay_user_to_admin(bot, message)

    # Foydalanuvchiga tasdiq
    await message.answer(MSG_AFTER_SUBMIT)


# =====================================================
# ADMIN → USER (reply orqali)
# =====================================================
@dp.message_handler(
    lambda m: m.chat.type == "private"
    and m.from_user.id == ADMIN_ID
    and m.reply_to_message,
    content_types=types.ContentTypes.ANY
)
async def handle_admin_reply(message: types.Message):
    await relay_admin_to_user(bot, message)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
