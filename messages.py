# messages.py
# =====================================================
# Bot tomonidan yuboriladigan barcha xabarlar
# =====================================================


# -----------------------------------------------------
# Ruxsat BOR foydalanuvchi uchun salomlashuv
# -----------------------------------------------------
MSG_WELCOME_ALLOWED = (
    "Assalomu alaykum 👋\n"
    "*Nargiza Olimovna* ning xususiy biriga xush kelibsiz.\n\n"
    "📌 Agar siz online guruh a’zosi bo‘lsangiz,\n"
    "yozgan esseyingizni *shu yerga* yuboring.\n\n"
    "❗️Iltimos, bo‘lib-bo‘lib emas, imkon bo‘lsa *bittada* yuboring.\n"
    "✍️ *Ism–familiya yozish esdan chiqmasin.*\n\n"
    "Men uni ustozga yetkazaman 🙂"
)


# -----------------------------------------------------
# Ruxsat YO‘Q foydalanuvchi uchun
# -----------------------------------------------------
MSG_NOT_ALLOWED = (
    "❌ *Afsuski*, siz *Nargiza Olimovna kursi* a’zosi emassiz.\n\n"
    "Shu sababli bot sizga xizmat ko‘rsata olmaydi."
)


# =====================================================
# ADMIN UCHUN XABARLAR
# =====================================================

# /boshlash — admin
MSG_ADMIN_STARTED = (
    "✅ *Esse qabul qilish OCHILDI.*\n\n"
    "Endi o‘quvchilar esse yuborishi mumkin."
)

# /yakun — admin
MSG_ADMIN_FINISHED = (
    "⛔ *Esse qabul qilish YOPILDI.*\n\n"
    "Endi yuborilgan esselar qabul qilinmaydi."
)


# =====================================================
# O‘QUVCHI UCHUN XABARLAR
# =====================================================

# Esse yuborilgandan keyin
MSG_ESSE_ACCEPTED = (
    "📌 *Esse yuborishni nihoyalagan bo‘lsangiz*, rahmat.\n"
    "⏳ 48 soat ichida tekshirib, esse guruhiga tashlanadi.\n\n"
    "✅ Yuborish yakunlanmagan bo‘lsa, *davom etavering*.\n"
    "Hamma sahifalarni tashlab qo‘ying."
)

# Esse qabul yopiq bo‘lsa
MSG_SUBMIT_CLOSED = (
    "❌ *Nargiza Olimovna esse qabul qilishni yakunladi.*\n\n"
    "Keyingi safar o‘z vaqtida ulgurishga harakat qiling.\n\n"
    "📩 Murojaatingiz bo‘lsa @Filolog_N ga yozing."
)


# -----------------------------------------------------
# Texnik xatolik
# -----------------------------------------------------
MSG_ERROR = (
    "❌ Texnik xatolik yuz berdi.\n"
    "Iltimos, birozdan so‘ng qayta urinib ko‘ring."
)
