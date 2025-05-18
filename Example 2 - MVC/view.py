# view.py

class TaskView:
    def show_menu(self):
        print("\n--- Lista de Tareas ---")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Eliminar tarea")
        print("4. Salir")

    def show_tasks(self, tasks):
        if not tasks:
            print("No hay tareas.")
        else:
            print("Tareas:")
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")

    def ask_for_task(self):
        return input("Ingresa la descripción de la tarea: ")

    def ask_for_index(self):
        return int(input("Ingresa el número de la tarea a eliminar: ")) - 1

    def show_message(self, message):
        print(message)
