from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بك في بوت الاهداءات الموسيقية! البوت يعمل الآن بنجاح 🎶")

if __name__ == '__main__':
    application = ApplicationBuilder().token("8428169374:AAGMi1fb7Fmjs2y8TmjVcAQ98_9woTjsZ_U").build()
    application.add_handler(CommandHandler('start', start))
    application.run_polling()
