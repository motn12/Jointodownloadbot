from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("TOKEN")  # توکن از محیط Railway میاد

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 ربات شما با موفقیت روی Railway اجرا شد!")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("ربات در حال اجراست...")
app.run_polling()  # یا اگر وب‌هوک میخوای، این خط رو عوض میکنیم
