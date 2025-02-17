import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

# استيراد الميزات من الملفات الأخرى
from features import get_matches, send_goal_notifications, get_news
from advanced_features import search_team, search_player, search_league, set_favorite_team, get_favorite_team
from extra_features import get_weekly_schedule, subscribe_to_team, unsubscribe_from_team, report_issue
from final_features import compare_players, predict_match_result, get_live_schedule, analyze_league, vote_for_match, get_votes
from leagues import get_leagues_menu
from streaming import get_live_stream_links
from notifications import enable_notifications, disable_notifications
from scheduled_notifications import register_match_interest
from match_highlights import get_match_highlights
from match_recommendations import get_top_matches
from trivia_quiz import get_trivia_question, check_trivia_answer
from betting_system import place_bet, check_bets
from user_rewards import add_user_points, get_top_users
from database import init_db

# إعدادات البوت
API_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# تهيئة قاعدة البيانات
init_db()

# 🔹 القائمة الرئيسية مع الأزرار التفاعلية
def main_menu():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("🏆 الدوريات", callback_data="leagues"),
        InlineKeyboardButton("⚽ المباريات", callback_data="matches"),
        InlineKeyboardButton("📺 البث المباشر", callback_data="live_stream"),
        InlineKeyboardButton("📊 الإحصائيات", callback_data="stats"),
        InlineKeyboardButton("🔍 البحث", callback_data="search"),
        InlineKeyboardButton("📰 الأخبار", callback_data="news"),
        InlineKeyboardButton("🔔 الإشعارات", callback_data="notifications"),
        InlineKeyboardButton("📅 جدول المباريات", callback_data="schedule"),
        InlineKeyboardButton("📢 التصويت", callback_data="vote"),
        InlineKeyboardButton("🏅 التحديات والجوائز", callback_data="challenges"),
        InlineKeyboardButton("📬 دعم المستخدم", callback_data="support"),
        InlineKeyboardButton("👨‍💻 المطور: علاء", url="https://t.me/your_telegram_username"),
    )
    return keyboard

# أمر البدء
@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.reply("🎉 أهلاً بك في بوت كرة القدم! اختر من القوائم أدناه:", reply_markup=main_menu())

# التعامل مع الأزرار
@dp.callback_query_handler(lambda call: True)
async def callback_handler(call: types.CallbackQuery):
    if call.data == "leagues":
        await call.message.edit_text("🏆 اختر الدوري:", reply_markup=get_leagues_menu())
    elif call.data == "matches":
        await call.message.edit_text("⚽ اختر نوع المباريات:", reply_markup=InlineKeyboardMarkup().add(
            InlineKeyboardButton("🔴 الجارية", callback_data="live_matches"),
            InlineKeyboardButton("🏁 القادمة", callback_data="upcoming_matches"),
            InlineKeyboardButton("✅ المنتهية", callback_data="finished_matches"),
            InlineKeyboardButton("🔙 العودة", callback_data="main_menu"),
        ))
    elif call.data == "search":
        await call.message.edit_text("🔍 أدخل اسم الفريق، اللاعب، أو الدوري:")
    elif call.data == "news":
        news = get_news()
        await call.message.edit_text(news, parse_mode="Markdown")
    elif call.data == "schedule":
        schedule = get_weekly_schedule()
        await call.message.edit_text(schedule, parse_mode="Markdown")
    elif call.data == "notifications":
        await call.message.edit_text("🔔 التحكم في الإشعارات:", reply_markup=InlineKeyboardMarkup().add(
            InlineKeyboardButton("✅ تفعيل", callback_data="enable_notifications"),
            InlineKeyboardButton("❌ تعطيل", callback_data="disable_notifications"),
            InlineKeyboardButton("🔙 العودة", callback_data="main_menu"),
        ))
    elif call.data == "vote":
        await call.message.edit_text("📢 أدخل معرف المباراة التي تريد التصويت لها:")
    elif call.data == "challenges":
        await call.message.edit_text("🏅 قائمة التحديات والجوائز:", reply_markup=InlineKeyboardMarkup().add(
            InlineKeyboardButton("🎯 تحدي التوقعات", callback_data="betting"),
            InlineKeyboardButton("🧠 اختبار المعلومات", callback_data="trivia"),
            InlineKeyboardButton("🏆 قائمة المتصدرين", callback_data="top_users"),
            InlineKeyboardButton("🔙 العودة", callback_data="main_menu"),
        ))

# تشغيل البوت
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp)
