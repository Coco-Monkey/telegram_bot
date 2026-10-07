# importar librerias de telegram
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler
)

from controllers.todoController import todoController

TOKEN = ""  # Llave del bot de telegram


# comando para crear la apliacion
application = ApplicationBuilder().token(TOKEN).build()

application.add_handler(CommandHandler("start", todoController.start))
application.add_handler(CommandHandler("add", todoController.add_Todo))
application.add_handler(CommandHandler("list", todoController.list_todos))
application.add_handler(CommandHandler("check", todoController.check_todo))
application.add_handler(CommandHandler("clear", todoController.delete_todo))
application.add_handler(CommandHandler("pop", todoController.pop))
application.add_handler(CommandHandler("update", todoController.update_todo))
application.add_handler(CommandHandler("uncheck", todoController.uncheck_todo))

application.add_handler(CallbackQueryHandler(todoController.button))

application.run_polling(allowed_updates=Update.ALL_TYPES)
