from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_leagues_menu():
    keyboard = InlineKeyboardMarkup(row_width=2)
    leagues = [
        "دوري أبطال أوروبا", "الدوري الإنجليزي", "الدوري الإسباني", "الدوري الإيطالي",
        "الدوري الألماني", "الدوري الفرنسي", "الدوري الجزائري", "كأس العالم",
        "دوري أبطال إفريقيا", "دوري أبطال آسيا", "كأس أمم إفريقيا", "كوبا ليبرتادوريس"
    ]
    for league in leagues:
        keyboard.add(InlineKeyboardButton(league, callback_data=f"league_{league}"))
    keyboard.add(InlineKeyboardButton("🔙 العودة", callback_data="main_menu"))
    return keyboard
