import sqlite3

def init_db():
    conn = sqlite3.connect("sports_bot.db")
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, notifications INTEGER)")
    cursor.execute("CREATE TABLE IF NOT EXISTS favorite_teams (user_id INTEGER, team_name TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS subscriptions (user_id INTEGER, team_name TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS votes (match_id INTEGER, user_id INTEGER, team_choice TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS notifications (user_id INTEGER, enabled INTEGER)")
    cursor.execute("CREATE TABLE IF NOT EXISTS betting (user_id INTEGER, match_id INTEGER, prediction TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS user_activity (user_id INTEGER, points INTEGER)")

    conn.commit()
    conn.close()
