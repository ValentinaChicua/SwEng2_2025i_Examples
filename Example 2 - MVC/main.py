# FrontEnd-Test.py

from model import TaskModel
from view import TaskView
from controller import TaskController

def main():
    model = TaskModel()
    view = TaskView()
    controller = TaskController(model, view)
    controller.run()

if __name__ == "__main__":
    main()
