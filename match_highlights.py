import requests

FOOTBALL_API_KEY = "YOUR_FOOTBALL_API_KEY"

# 🔹 جلب ملخص المباراة
def get_match_highlights(match_id):
    url = f"https://v3.football.api-sports.io/highlights?fixture={match_id}"
    headers = {"x-apisports-key": FOOTBALL_API_KEY}
    response = requests.get(url, headers=headers).json()

    if response["response"]:
        highlights = response["response"][0]
        return f"🎥 **ملخص المباراة:**\n\n⚽ الأهداف: {highlights['goals']}\n🎯 التمريرات الحاسمة: {highlights['assists']}\n📹 شاهد الملخص هنا: {highlights['video_url']}"
    else:
        return "❌ لا يوجد ملخص لهذه المباراة حتى الآن."
