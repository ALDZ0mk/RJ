import requests

FOOTBALL_API_KEY = "YOUR_FOOTBALL_API_KEY"

# 🔹 جلب روابط البث المباشر
def get_live_stream_links(match_id):
    url = f"https://v3.football.api-sports.io/streams?fixture={match_id}"
    headers = {"x-apisports-key": FOOTBALL_API_KEY}
    response = requests.get(url, headers=headers).json()

    if response["response"]:
        links = response["response"][0]["streams"]
        message = "🎥 **روابط البث المباشر:**\n\n"
        for link in links:
            message += f"🔗 [{link['name']}]({link['url']})\n"
        return message
    else:
        return "❌ لا توجد روابط بث متاحة حاليًا."
