import random

# 🔹 أسئلة التحدي الكروي
trivia_questions = [
    {"question": "من هو أكثر لاعب سجل أهداف في كأس العالم؟", "options": ["بيليه", "رونالدو", "كلوزه", "ميسي"], "answer": "كلوزه"},
    {"question": "أي فريق فاز بأكبر عدد من بطولات دوري أبطال أوروبا؟", "options": ["برشلونة", "مانشستر يونايتد", "ريال مدريد", "بايرن ميونيخ"], "answer": "ريال مدريد"},
    {"question": "في أي سنة أقيمت أول بطولة لكأس العالم؟", "options": ["1930", "1950", "1925", "1960"], "answer": "1930"},
]

# 🔹 اختيار سؤال عشوائي
def get_trivia_question():
    question = random.choice(trivia_questions)
    return f"🧠 **اختبار معلومات كرة القدم**\n\n❓ {question['question']}\n\n🔹 {question['options'][0]}\n🔹 {question['options'][1]}\n🔹 {question['options'][2]}\n🔹 {question['options'][3]}"

# 🔹 التحقق من الإجابة
def check_trivia_answer(question_text, user_answer):
    for question in trivia_questions:
        if question["question"] == question_text:
            return "✅ إجابة صحيحة!" if user_answer == question["answer"] else "❌ إجابة خاطئة، حاول مرة أخرى!"
    return "❌ السؤال غير موجود."
