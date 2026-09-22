from telegram import Update
from telegram.ext import ContextTypes

from modelos.todo import Todo
from modelos.todoList import todo_list


class todoController:

    @staticmethod
    async def add_Todo(update: Update, context: ContextTypes.DEFAULT_TYPE):
        command = update.message.text.split()[0]
        title = "".join(update.message.text.split(command)[1])
        todo_list.append(Todo(title))
        await update.message.reply_text(f"se agrego la tarea: {title}") 

    @staticmethod
    async def list_todos(update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not todo_list:
            await update.message.reply_text("No hay tareas todavia")
        else:
            tasks = "\n".join([f"{i+1}. {todo.title}" for i, todo in enumerate(todo_list)])
            await update.message.reply_text(f"Tareas pendientes:\n{tasks}")


    @staticmethod
    async def check_todo(update: Update, context: ContextTypes.DEFAULT_TYPE):
        index = int(context.args[0])
        if (index < 1) or (index > len(todo_list)):
            await update.message.reply_text("ERROR: esa tarea no existe, por favor ingrese un numero valido")
        elif todo_list[index-1]:
            await update.message.reply_text(f"Tarea: \"{todo_list[index-1].title}\" completada!")
            todo_list.pop(index-1)
            await update.message.reply_text(f"Lista de tareas actualizada:\n" + "\n".join([f"{i+1}. {todo.title}" for i, todo in enumerate(todo_list)]))