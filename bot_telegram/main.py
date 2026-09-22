#importar librerias de telegram
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from controllers.todoController import todoController

TOKEN = "" #Llave del bot de telegram

    
#comando para crear la apliacion
application = ApplicationBuilder().token(TOKEN).build()


application.add_handler(CommandHandler("add", todoController.add_Todo))
application.add_handler(CommandHandler("list", todoController.list_todos))
application.add_handler(CommandHandler('check', todoController.check_todo))

application.run_polling(allowed_updates=Update.ALL_TYPES)