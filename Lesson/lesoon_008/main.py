from telegram import Update
from telegram.ext import updater, CommandHandler, ContextTypes,


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("5636284208:AAEbIXEwY_wkXPL1aHnHWWlUmP1yotOXMGM").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()