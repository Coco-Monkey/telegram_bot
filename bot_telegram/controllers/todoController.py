from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

from modelos.todo import Todo
from modelos.todoList import todo_list


class todoController:
    
    @staticmethod
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Manda un mensaje con tres opciones"""
        keyboard = [
            [
                InlineKeyboardButton("start", callback_data= "1"),
            ],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text("Please choose", reply_markup=reply_markup)


    """
    @staticmethod
    async def add_Todo_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
        #Manda un mensaje con tres opciones#
        keyboard = [
            [
                InlineKeyboardButton("Agregar tarea", callback_data= "2"),
            ],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text("Please choose", reply_markup=reply_markup)
    """


    @staticmethod
    async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
        #Parses the CallbackQuery and updates the message text.
        query = update.callback_query

        await query.answer()

        await todoController.say_hi(update, context)
        #await todoController.add_Todo_button(update, context)




    @staticmethod
    async def say_hi(update: Update, context: ContextTypes.DEFAULT_TYPE):
            query = update.callback_query

            await query.edit_message_text("Hola, bienvenido al bot de tareas, los comandos disponibles son:\n")



    # agregar tarea
    @staticmethod
    async def add_Todo(update: Update, context: ContextTypes.DEFAULT_TYPE):
        command = update.message.text.split()[0]
        title = "".join(update.message.text.split(command)[1])
        if title == "":
            await update.message.reply_text(
                "Error: no se puede ingresar tareas vacias, porfavor ingresa una tarea valida"
            )
        else:
            todo_list.append(Todo(title))
            await update.message.reply_text(f"se agrego la tarea: {title}")

    # listar las tareas
    @staticmethod
    async def list_todos(update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not todo_list:
            await update.message.reply_text("No hay tareas todavia")
        else:
            tasks = ""
            for i, todo in enumerate(todo_list):
                tasks += (
                    f"{i + 1} - {'✅' if todo.is_completed else '🚫'} {todo.title}\n"
                )
            await update.message.reply_text(f"Tareas pendientes:\n{tasks}")

    # actualizar tareas
    @staticmethod
    async def update_todo(update: Update, context: ContextTypes.DEFAULT_TYPE):
        index = int(context.args[0])
        command = update.message.text.split()[1]
        new_title = "".join(update.message.text.split(command)[1:])
        if (index < 1) or (index > len(todo_list) or (index == 0)):
            await update.message.reply_text(
                "ERROR: esa tarea no existe, por favor ingrese un numero valido"
            )
        else:
            todo_list[index - 1].title = new_title
            todo_list[index - 1].is_completed = False
            await update.message.reply_text(f"Tarea {index} actualizada a: {new_title}")
            await todoController.list_todos(
                update, context
            )  # concatenacion de funciones/controladores para mostrar la lista de tareas despues de actualizar una tarea

    # marcar una tarea como completada
    @staticmethod
    async def check_todo(update: Update, context: ContextTypes.DEFAULT_TYPE):
        index = int(context.args[0])
        if (index < 1) or (index > len(todo_list) or (index == 0)):
            await update.message.reply_text(
                "ERROR: esa tarea no existe, por favor ingrese un numero valido"
            )
        else:
            todo_list[index - 1].is_completed = True
            await update.message.reply_text(
                f'Tarea: "{todo_list[index - 1].title}" completada!'
            )
            await todoController.list_todos(
                update, context
            )  # concatenacion de funciones/controladores para mostrar la lista de tareas despues de marcar una como completada

    # borrar todas las tareas
    @staticmethod
    async def delete_todo(update: Update, context: ContextTypes.DEFAULT_TYPE):
        todo_list.clear()
        await update.message.reply_text("Todas las tareas han sido eliminadas")

    # borrar una tarea especifica
    @staticmethod
    async def pop(update: Update, context: ContextTypes.DEFAULT_TYPE):
        if context.args:
            index = int(context.args[0])
            if (index < 1) or (index > len(todo_list)):
                await update.message.reply_text(
                    "ERROR: esa tarea no existe, por favor ingrese un numero valido"
                )
            else:
                deleted_task = todo_list.pop(index - 1)
                await update.message.reply_text(
                    f'Tarea: "{deleted_task.title}" eliminada!'
                )
                await todoController.list_todos(update, context)

    # Desmarcar tarea
    @staticmethod
    async def uncheck_todo(update: Update, context: ContextTypes.DEFAULT_TYPE):
        if context.args:
            index = int(context.args[0])
            if (index < 0) or (index > len(todo_list) or (index == 0)):
                await update.message.reply_text(
                    "ERROR: esa tarea no existe, por favor ingrese un numero de tarea valido"
                )
            else:
                if todo_list[index - 1].is_completed == False:
                    await update.message.reply_text("Esa tarea esta sin aun completar")
                    await todoController.list_todos(update, context)
                else:
                    uncheck_task = todo_list[index - 1]
                    uncheck_task.is_completed = False
                    await update.message.reply_text(
                        f'Tarea: "{uncheck_task.title}" desmarcada'
                    )
                    await todoController.list_todos(update, context)
        else:
            await update.message.reply_text(
                "ERROR: Esa tarea no existe, porfavor ingrese un numero de tarea valido"
            )
