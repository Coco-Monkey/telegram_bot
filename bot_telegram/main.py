#importar librerias de telegram
from tracemalloc import start
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8612239577:AAFefHtmVZdPo301FCgESNEvCNDcGYojzhw"

#crear la aplicacion

#mensaje al iniciar el bot
async def say_hi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello human!")

#echo
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

#comando para crear la apliacion
application = ApplicationBuilder().token(TOKEN).build()


application.add_handler(CommandHandler("Hello", say_hi))
application.add_handler(CommandHandler("echo", echo))

application.run_polling(allowed_updates=Update.ALL_TYPES)