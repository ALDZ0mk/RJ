import requests

FOOTBALL_API_KEY = "YOUR_FOOTBALL_API_KEY"

# 🔹 جلب جدول المباريات للأسبوع القادم
def get_weekly_schedule():
    url = "https://v3.football.api-sports.io/fixtures?next=7"
    headers = {"x-apisports-key": FOOTBALL_API_KEY}
    matches = requests.get(url, headers=headers).json()

    schedule = "📅 **جدول المباريات للأسبوع القادم:**\n\n"
    for match in matches["response"]:
        schedule += f"🏆 {match['league']['name']}\n⚽ {match['teams']['home']['name']} 🆚 {match['teams']['away']['name']}\n🕐 {match['fixture']['date']}\n\n"

    return schedule
