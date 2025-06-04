from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# این توکن رو از BotFather بگیر و جایگزین کن
BOT_TOKEN = '7548887933:AAGlhiC7osC6DX9GjTLai_a5GpxuFFBOetc'

# هندلر پیام‌های متنی
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.lower()
    if user_message == 'سلام':
        await update.message.reply_text('سلام علیک!')
    else:
        await update.message.reply_text('فقط سلامو می‌فهمم 😅')

# هندلر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('سلام! من یه مینی‌باتم. بهم سلام کن!')

# اجرای ربات
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("ربات روشنه...")
    app.run_polling()

if __name__ == '__main__':
    main()
