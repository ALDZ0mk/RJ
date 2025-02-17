import requests

FOOTBALL_API_KEY = "YOUR_FOOTBALL_API_KEY"

# 🔹 اقتراح المباريات القوية
def get_top_matches():
    url = "https://v3.football.api-sports.io/fixtures?date=today"
    headers = {"x-apisports-key": FOOTBALL_API_KEY}
    response = requests.get(url, headers=headers).json()

    top_matches = []
    for match in response["response"]:
        if match["importance"] >= 8:
            top_matches.append(f"🔥 **{match['teams']['home']['name']} 🆚 {match['teams']['away']['name']}**\n🏆 البطولة: {match['league']['name']}\n⏰ التوقيت: {match['fixture']['date']}")

    return "\n\n".join(top_matches) if top_matches else "❌ لا توجد مباريات قوية اليوم."
