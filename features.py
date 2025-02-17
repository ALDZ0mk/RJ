import os
import requests
import asyncio
from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

# ✅ تحميل المفاتيح من المتغيرات البيئية
FOOTBALL_API_KEY = os.getenv("FOOTBALL_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")  # معرف القناة

# ✅ التأكد من أن جميع المفاتيح مضبوطة
if not FOOTBALL_API_KEY or not NEWS_API_KEY or not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHANNEL_ID:
    raise ValueError("❌ تأكد من ضبط المتغيرات البيئية: FOOTBALL_API_KEY, NEWS_API_KEY, TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL_ID")

# ✅ تهيئة البوت والجدولة
bot = Bot(token=TELEGRAM_BOT_TOKEN)
scheduler = AsyncIOScheduler()

# 🔹 جلب المباريات الجارية الآن
def get_matches():
    url = "https://v3.football.api-sports.io/fixtures?live=all"
    headers = {"x-apisports-key": FOOTBALL_API_KEY}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        matches_list = []
        for match in data.get("response", []):
            home = match["teams"]["home"]["name"]
            away = match["teams"]["away"]["name"]
            score = f"{match['goals']['home']} - {match['goals']['away']}"
            matches_list.append(f"⚽ {home} 🆚 {away} | 🏆 النتيجة: {score}")

        return "\n".join(matches_list) if matches_list else "❌ لا توجد مباريات جارية الآن."

    except requests.exceptions.RequestException as e:
        return f"❌ خطأ في جلب المباريات: {e}"

# 🔹 جلب الأخبار الرياضية
def get_news():
    url = f"https://newsapi.org/v2/top-headlines?category=sports&language=ar&apiKey={NEWS_API_KEY}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        news_list = []
        for article in data.get("articles", [])[:5]:
            news_list.append(f"📰 {article['title']}\n🔗 [اقرأ المزيد]({article['url']})")

        return "\n\n".join(news_list) if news_list else "❌ لا توجد أخبار متاحة."

    except requests.exceptions.RequestException as e:
        return f"❌ خطأ في جلب الأخبار: {e}"

# 🔹 جدولة إرسال الإشعارات
async def send_goal_notifications():
    matches = get_matches()
    try:
        await bot.send_message(chat_id=TELEGRAM_CHANNEL_ID, text=matches)
    except Exception as e:
        print(f"❌ خطأ أثناء إرسال الرسالة: {e}")

# ✅ تشغيل الجدولة داخل `async def main()`
async def start_scheduler():
    print("✅ بدء تشغيل الجدولة...")
    scheduler.add_job(send_goal_notifications, "interval", minutes=3)
    scheduler.start()

if __name__ == "__main__":
    asyncio.run(start_scheduler())
