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
            await update.message.reply_text("No hay tareas pendientes.")
        else:
            tasks = "\n".join([f"{i+1}. {todo.title}" for i, todo in enumerate(todo_list)])
            await update.message.reply_text(f"Tareas pendientes:\n{tasks}")