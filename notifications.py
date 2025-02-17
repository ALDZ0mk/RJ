import sqlite3
from aiogram import Bot

bot = Bot(token="YOUR_TELEGRAM_BOT_TOKEN")

# قاعدة بيانات لحفظ إعدادات الإشعارات
conn = sqlite3.connect("sports_bot.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS notifications (user_id INTEGER, enabled INTEGER)")
conn.commit()

# 🔹 تفعيل الإشعارات
def enable_notifications(user_id):
    cursor.execute("INSERT OR REPLACE INTO notifications (user_id, enabled) VALUES (?, 1)", (user_id,))
    conn.commit()

# 🔹 تعطيل الإشعارات
def disable_notifications(user_id):
    cursor.execute("INSERT OR REPLACE INTO notifications (user_id, enabled) VALUES (?, 0)", (user_id,))
    conn.commit()
