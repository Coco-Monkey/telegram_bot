from telegram import Update
from telegram.ext import ContextTypes

from modelos import todo
from modelos.todo import Todo
from modelos.todoList import todo_list


class todoController:

    @staticmethod
    async def say_hi(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Hola humano, los comandos disponibles son:\n"
                                                "/start - Inicia el bot y muestra un mensaje de bienvenida\n"
                                                "/add <tarea> - Agrega una nueva tarea a la lista\n"
                                                "/list - Muestra todas las tareas pendientes\n"
                                                "/check <numero> - Marca una tarea como completada\n"
                                                "/clear - Elimina todas las tareas de la lista\n"
                                                "/pop <numero> - Elimina una tarea especifica de la lista\n"
                                                "/update <numero> <nueva tarea> - Actualiza el titulo de una tarea especifica\n")



    #agregar tarea
    @staticmethod
    async def add_Todo(update: Update, context: ContextTypes.DEFAULT_TYPE):
        command = update.message.text.split()[0]
        title = "".join(update.message.text.split(command)[1])
        if title == "":
            await update.message.reply_text("Error: no se puede ingresar tareas vacias, porfavor ingresa una tarea valida")
        else:
            todo_list.append(Todo(title))
            await update.message.reply_text(f"se agrego la tarea: {title}")



    #listar las tareas
    @staticmethod
    async def list_todos(update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not todo_list:
            await update.message.reply_text("No hay tareas todavia")
        else:
            tasks = ""
            for i, todo in enumerate(todo_list):
                tasks += f"{i+1} - { "✅" if todo.is_completed else "🚫" } {todo.title}\n"
            await update.message.reply_text(f"Tareas pendientes:\n{tasks}")



    #actualizar tareas
    @staticmethod
    async def update_todo(update: Update, context: ContextTypes.DEFAULT_TYPE):
        index = int(context.args[0])
        command = update.message.text.split()[1]
        new_title = "".join(update.message.text.split(command)[1:])
        if (index < 1) or (index > len(todo_list) or (index == 0)):
            await update.message.reply_text("ERROR: esa tarea no existe, por favor ingrese un numero valido")
        else:
            todo_list[index-1].title = new_title
            todo_list[index-1].is_completed = False
            await update.message.reply_text(f"Tarea {index} actualizada a: {new_title}")
            await todoController.list_todos(update, context) #concatenacion de funciones/controladores para mostrar la lista de tareas despues de actualizar una tarea



    #marcar una tarea como completada
    @staticmethod
    async def check_todo(update: Update, context: ContextTypes.DEFAULT_TYPE):
        index = int(context.args[0])
        if (index < 1) or (index > len(todo_list) or (index == 0)):
            await update.message.reply_text("ERROR: esa tarea no existe, por favor ingrese un numero valido")
        else:
            todo_list[index-1].is_completed = True
            await update.message.reply_text(f"Tarea: \"{todo_list[index-1].title}\" completada!")
            await todoController.list_todos(update, context) #concatenacion de funciones/controladores para mostrar la lista de tareas despues de marcar una como completada



    #borrar todas las tareas
    @staticmethod
    async def delete_todo(update: Update, context: ContextTypes.DEFAULT_TYPE):
        todo_list.clear()
        await update.message.reply_text("Todas las tareas han sido eliminadas")



    #borrar una tarea especifica
    @staticmethod
    async def pop(update: Update, context: ContextTypes.DEFAULT_TYPE):
        if context.args:
            index = int(context.args[0])
            if (index < 1) or (index > len(todo_list)):
                await update.message.reply_text("ERROR: esa tarea no existe, por favor ingrese un numero valido")
            else:
                deleted_task = todo_list.pop(index-1)
                await update.message.reply_text(f"Tarea: \"{deleted_task.title}\" eliminada!")
                await todoController.list_todos(update, context)


