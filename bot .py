import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 أهلاً بك في Sellora AI!\n\n"
        "أنا مساعدك الذكي. قريباً رح أقدر أساعدك بالتسويق وكتابة المحتوى."
    )


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 وصلتني رسالتك!\n\n"
        "Sellora AI قيد التجهيز، ورح نضيف الذكاء الاصطناعي قريباً."
    )


def main():
    if not TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN is not set")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message))

    print("Sellora AI is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
