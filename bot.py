import os
import telebot
from google import genai

# جلب مفاتيح الاتصال من بيئة التشغيل (لحماية خصوصيتك)
BOT_TOKEN = os.environ.get('BOT_TOKEN')
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')

# تشغيل البوت والذكاء الاصطناعي
bot = telebot.TeleBot(BOT_TOKEN)
ai_client = genai.Client(api_key=GEMINI_API_KEY)

# الرد على أمر /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! أنا بوت مدعوم بالذكاء الاصطناعي. اسألني عن أي شيء وسأجيبك فوراً! 🤖")

# استقبال رسائل المستخدم وتمريرها للذكاء الاصطناعي
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # إرسال إشارة للمستخدم أن البوت "يكتب الآن..."
        bot.send_chat_action(message.chat.id, 'typing')
        
        # إرسال النص إلى نموذج الجيمني
        response = ai_client.models.generate_content(
            model='gemini-2.5-flash',
            contents=message.text,
        )
        
        # إرسال رد الذكاء الاصطناعي للمستخدم
        bot.reply_to(message, response.text)
        
    except Exception as e:
        bot.reply_to(message, "عذراً، حدث خطأ أثناء معالجة طلبك. حاول مجدداً لاحقاً.")
        print(f"Error: {e}")

# تشغيل البوت بشكل مستمر
if __name__ == '__main__':
    print("البوت يعمل الآن...")
    bot.infinity_polling()
