import requests
from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

FOOTBALL_API_KEY = "YOUR_FOOTBALL_API_KEY"
bot = Bot(token="YOUR_TELEGRAM_BOT_TOKEN")
scheduler = AsyncIOScheduler()

# 🔹 جلب المباريات الجارية الآن
def get_matches():
    url = "https://v3.football.api-sports.io/fixtures?live=all"
    headers = {"x-apisports-key": FOOTBALL_API_KEY}
    response = requests.get(url, headers=headers).json()
    
    matches_list = []
    for match in response["response"]:
        home = match["teams"]["home"]["name"]
        away = match["teams"]["away"]["name"]
        score = f"{match['goals']['home']} - {match['goals']['away']}"
        matches_list.append(f"⚽ {home} 🆚 {away} | 🏆 النتيجة: {score}")

    return "\n".join(matches_list) if matches_list else "❌ لا توجد مباريات جارية الآن."

# 🔹 جلب الأخبار الرياضية
def get_news():
    url = "https://newsapi.org/v2/top-headlines?category=sports&language=ar&apiKey=YOUR_NEWS_API_KEY"
    response = requests.get(url).json()
    
    news_list = []
    for article in response["articles"][:5]:
        news_list.append(f"📰 {article['title']}\n🔗 [اقرأ المزيد]({article['url']})")

    return "\n\n".join(news_list) if news_list else "❌ لا توجد أخبار متاحة."

# 🔹 جدولة إرسال الإشعارات
async def send_goal_notifications():
    matches = get_matches()
    await bot.send_message(chat_id="@your_channel", text=matches)

scheduler.add_job(send_goal_notifications, "interval", minutes=3)
scheduler.start()
