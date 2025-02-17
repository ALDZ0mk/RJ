import requests
import sqlite3
from datetime import datetime, timedelta
from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

FOOTBALL_API_KEY = "YOUR_FOOTBALL_API_KEY"
bot = Bot(token="YOUR_TELEGRAM_BOT_TOKEN")
scheduler = AsyncIOScheduler()

# قاعدة بيانات لحفظ الاشتراكات في المباريات المهمة
conn = sqlite3.connect("sports_bot.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS match_notifications (user_id INTEGER, match_id INTEGER)")
conn.commit()

# 🔹 إرسال تذكير بالمباريات المهمة
async def send_match_reminders():
    url = "https://v3.football.api-sports.io/fixtures?date=today"
    headers = {"x-apisports-key": FOOTBALL_API_KEY}
    matches = requests.get(url, headers=headers).json()

    for match in matches["response"]:
        match_time = datetime.strptime(match["fixture"]["date"], "%Y-%m-%dT%H:%M:%S%z")
        if match_time - timedelta(minutes=30) < datetime.now():
            users = cursor.execute("SELECT user_id FROM match_notifications WHERE match_id=?", (match["fixture"]["id"],)).fetchall()
            for user in users:
                await bot.send_message(chat_id=user[0], text=f"⏳ تذكير: مباراة {match['teams']['home']['name']} ضد {match['teams']['away']['name']} تبدأ خلال 30 دقيقة!")

scheduler.add_job(send_match_reminders, "interval", minutes=15)
scheduler.start()
import requests
import sqlite3
from datetime import datetime, timedelta
from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

FOOTBALL_API_KEY = "YOUR_FOOTBALL_API_KEY"
bot = Bot(token="YOUR_TELEGRAM_BOT_TOKEN")
scheduler = AsyncIOScheduler()

# قاعدة بيانات لحفظ الاشتراكات في المباريات المهمة
conn = sqlite3.connect("sports_bot.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS match_notifications (user_id INTEGER, match_id INTEGER)")
conn.commit()

# 🔹 إرسال تذكير بالمباريات المهمة
async def send_match_reminders():
    url = "https://v3.football.api-sports.io/fixtures?date=today"
    headers = {"x-apisports-key": FOOTBALL_API_KEY}
    matches = requests.get(url, headers=headers).json()

    for match in matches["response"]:
        match_time = datetime.strptime(match["fixture"]["date"], "%Y-%m-%dT%H:%M:%S%z")
        if match_time - timedelta(minutes=30) < datetime.now():
            users = cursor.execute("SELECT user_id FROM match_notifications WHERE match_id=?", (match["fixture"]["id"],)).fetchall()
            for user in users:
                await bot.send_message(chat_id=user[0], text=f"⏳ تذكير: مباراة {match['teams']['home']['name']} ضد {match['teams']['away']['name']} تبدأ خلال 30 دقيقة!")

scheduler.add_job(send_match_reminders, "interval", minutes=15)
scheduler.start()
