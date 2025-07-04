from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from responses import reaction_functions
import os

# بررسی اینکه آیا کاربر ادمین گروه هست یا نه
async def is_user_admin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    try:
        chat_id = update.effective_chat.id
        user_id = update.effective_user.id
        admins = await context.bot.get_chat_administrators(chat_id)
        return any(admin.user.id == user_id for admin in admins)
    except:
        return False

# تابع اصلی برای پردازش پیام‌ها
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text.lower()
    user = update.message.from_user
    username = user.first_name or user.username or "دوست من"

    is_reply_to_bot = (
        update.message.reply_to_message and
        update.message.reply_to_message.from_user and
        update.message.reply_to_message.from_user.is_bot
    )

    mentioned_joker = "جوکر" in text
    is_admin = await is_user_admin(update, context)

    for func in reaction_functions:
        try:
            response = func(text, is_admin=is_admin)
        except TypeError:
            response = func(text)
        if response:
            prefix = f"{username}..." if is_reply_to_bot or mentioned_joker else ""
            await update.message.reply_text(f"{prefix} {response}".strip())
            return

# اجرای بات
if __name__ == '__main__':
    TOKEN = os.environ.get("JOKER_TOKEN")  # یا مستقیم بنویس: TOKEN = "توکن_بات_تو"
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("🃏 مستر جوک آنلاین شد...")
    app.run_polling()
