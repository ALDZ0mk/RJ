import sqlite3

conn = sqlite3.connect("sports_bot.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS user_activity (user_id INTEGER, points INTEGER)")
conn.commit()

# 🔹 تسجيل نقاط المستخدمين
def add_user_points(user_id, points):
    cursor.execute("INSERT INTO user_activity (user_id, points) VALUES (?, ?) ON CONFLICT(user_id) DO UPDATE SET points = points + ?", (user_id, points, points))
    conn.commit()

# 🔹 عرض أفضل المستخدمين
def get_top_users():
    cursor.execute("SELECT user_id, points FROM user_activity ORDER BY points DESC LIMIT 5")
    results = cursor.fetchall()
    return "\n".join([f"🏅 المستخدم {result[0]}: {result[1]} نقطة" for result in results]) if results else "❌ لا يوجد نشاط كافٍ بعد."
