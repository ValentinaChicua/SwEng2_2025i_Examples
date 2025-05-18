# model.py

class TaskModel:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(description)

    def get_tasks(self):
        return self.tasks

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            raise IndexError("Índice fuera de rango.")