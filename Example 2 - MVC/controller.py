# controller.py

class TaskController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        while True:
            self.view.show_menu()
            choice = input("Selecciona una opción: ")

            if choice == "1":
                tasks = self.model.get_tasks()
                self.view.show_tasks(tasks)

            elif choice == "2":
                task = self.view.ask_for_task()
                self.model.add_task(task)
                self.view.show_message("Tarea agregada.")

            elif choice == "3":
                try:
                    index = self.view.ask_for_index()
                    self.model.delete_task(index)
                    self.view.show_message("Tarea eliminada.")
                except (ValueError, IndexError):
                    self.view.show_message("Error: índice inválido.")

            elif choice == "4":
                self.view.show_message("¡Hasta luego!")
                break

            else:
                self.view.show_message("Opción inválida. Intenta de nuevo.")
