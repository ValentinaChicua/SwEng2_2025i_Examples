
# 🗂️ To-Do App (MVC Pattern in Python)

This is a console-based to-do list application built in Python that follows the **MVC (Model - View - Controller)** architectural pattern. It is ideal for learning how to separate responsibilities in software design.

## 📚 Objectives

- Understand and implement the MVC pattern in Python.
- Separate concerns into model (data), view (UI), and controller (logic).
- Write clean, maintainable, and modular code.

---

## 📁 Project Structure

```
todo_app/
├── controller.py   # Logic that coordinates model and view
├── model.py        # Task management (data)
├── view.py         # User interface (input/output)
└── main.py         # Application entry point
```

---

## ▶️ How to Run

1. Clone the repository or download the files into a directory named `todo_app`.

2. Run the application using Python 3:

```bash
python FrontEnd-Test.py
```

---

## 💻 Features

From the console menu, you can:

1. View existing tasks  
2. Add a new task  
3. Delete a task by number  
4. Exit the application

---

## 🧠 How MVC is Implemented

| Component   | File           | Main Responsibility                          |
|------------|----------------|-----------------------------------------------|
| Model      | `model.py`     | Manages tasks (add, delete, list)             |
| View       | `view.py`      | Handles user interface and display            |
| Controller | `controller.py`| Orchestrates input and updates between M/V    |

---

## 🧩 Suggested Extensions (for lab assignments)

- [ ] Save/load tasks from a `.json` file
- [ ] Prevent duplicate tasks
- [ ] Add "completed" status to tasks
- [ ] Replace CLI with GUI using Tkinter or Flask (MVC with interface)

---


