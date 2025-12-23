# state.py
# =====================================================
# Esse qabul qilish umumiy holati (ADMIN boshqaradi)
# =====================================================

# possible states: "closed", "open"
SUBMIT_STATE = "closed"


def is_open() -> bool:
    return SUBMIT_STATE == "open"


def open_submit():
    global SUBMIT_STATE
    SUBMIT_STATE = "open"


def close_submit():
    global SUBMIT_STATE
    SUBMIT_STATE = "closed"
