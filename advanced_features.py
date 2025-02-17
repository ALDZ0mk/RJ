import requests

FOOTBALL_API_KEY = "YOUR_FOOTBALL_API_KEY"

# 🔎 البحث عن لاعب
def search_player(player_name):
    url = f"https://v3.football.api-sports.io/players?search={player_name}"
    headers = {"x-apisports-key": FOOTBALL_API_KEY}
    response = requests.get(url, headers=headers).json()

    if response["response"]:
        player = response["response"][0]["player"]
        return f"⚽ {player['name']} - {player['team']['name']}\n🎂 العمر: {player['age']}\n🏅 المركز: {player['position']}\n🎯 الأهداف: {player['statistics'][0]['goals']['total']}"
    else:
        return "❌ لم يتم العثور على اللاعب."

# 🔎 البحث عن فريق
def search_team(team_name):
    url = f"https://v3.football.api-sports.io/teams?search={team_name}"
    headers = {"x-apisports-key": FOOTBALL_API_KEY}
    response = requests.get(url, headers=headers).json()

    if response["response"]:
        team = response["response"][0]
        return f"🏆 {team['team']['name']} - {team['team']['country']}\n📅 تأسس عام {team['team']['founded']}\n🏟️ ملعب: {team['venue']['name']}"
    else:
        return "❌ لم يتم العثور على الفريق."
