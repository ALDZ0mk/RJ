import sqlite3

conn = sqlite3.connect("sports_bot.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS betting (user_id INTEGER, match_id INTEGER, prediction TEXT)")
conn.commit()

# 🔹 تسجيل توقع المستخدم
def place_bet(user_id, match_id, prediction):
    cursor.execute("INSERT INTO betting (user_id, match_id, prediction) VALUES (?, ?, ?)", (user_id, match_id, prediction))
    conn.commit()

# 🔹 حساب النتائج بعد المباراة
def check_bets(match_id, actual_result):
    cursor.execute("SELECT user_id, prediction FROM betting WHERE match_id=?", (match_id,))
    bets = cursor.fetchall()
    winners = [user_id for user_id, prediction in bets if prediction == actual_result]
    return winners if winners else []
