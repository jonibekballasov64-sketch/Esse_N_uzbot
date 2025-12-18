# config.py
# =====================================================
# Bot uchun asosiy sozlamalar
# =====================================================

import os


# =====================================================
# Telegram bot token
# Railway’da ENV orqali beriladi
# =====================================================
BOT_TOKEN = os.getenv("BOT_TOKEN", "")


# =====================================================
# Admin (sizning shaxsiy Telegram ID)
# Barcha esselar shu akkauntga keladi
# =====================================================
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))


# =====================================================
# Kurs nomi (xabar matnlarida ishlatiladi)
# =====================================================
COURSE_NAME = "Nargiza Olimovna kursi"


# =====================================================
# Esse tekshiruv muddati (soatlarda)
# Faqat xabarlarda ko‘rinadi
# =====================================================
CHECK_HOURS = 48


# =====================================================
# Kimga yuborildi deb ko‘rinishi
# =====================================================
REVIEW_USERNAME = "@Filolog_N"
