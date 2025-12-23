# state.py
# =====================================================
# Foydalanuvchi esse topshirish holati
# =====================================================

# user_id -> state
# state: "idle" | "started" | "finished"
USER_STATES = {}


def get_state(user_id: int) -> str:
    """
    Foydalanuvchining joriy holatini qaytaradi
    """
    return USER_STATES.get(user_id, "idle")


def set_state(user_id: int, state: str):
    """
    Foydalanuvchi holatini o‘zgartiradi
    """
    USER_STATES[user_id] = state


def reset_state(user_id: int):
    """
    Foydalanuvchini boshlang‘ich holatga qaytaradi
    """
    USER_STATES.pop(user_id, None)
