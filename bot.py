import os
import telebot
import requests

# جلب توكن البوت من بيئة التشغيل
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

# الرد على أمر /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! أنا بوت مدعوم بالذكاء الاصطناعي المفتوح. اسألني عن أي شيء وسأجيبك فوراً! 🤖")

# استقبال رسائل المستخدم وتمريرها للذكاء الاصطناعي (بدون حظر وبدون مفتاح)
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # إشارة بأن البوت يكتب...
        bot.send_chat_action(message.chat.id, 'typing')
        
        # الاتصال بالذكاء الاصطناعي عبر خادم مفتوح
        api_url = f"https://ddns.net{requests.utils.quote(message.text)}"
        response = requests.get(api_url, timeout=15)
        
        if response.status_code == 200:
            ai_response = response.json().get('response', 'لم أستطع فهم ذلك.')
            bot.reply_to(message, ai_response)
        else:
            bot.reply_to(message, "عذراً، الخادم مشغول حالياً. حاول مجدداً بعد قليل.")
            
    except Exception as e:
        bot.reply_to(message, "عذراً، حدث خطأ أثناء معالجة طلبك. حاول مجدداً لاحقاً.")
        print(f"Error: {e}")

# تشغيل البوت بشكل مستمر
if __name__ == '__main__':
    print("البوت يعمل الآن...")
    bot.infinity_polling()
