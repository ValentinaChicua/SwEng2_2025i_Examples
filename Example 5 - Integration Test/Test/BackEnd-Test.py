import requests

# Endpoints
USERS_URL = "http://localhost:5001/users"
TASKS_URL = "http://localhost:5002/tasks"

def create_user(name):
    response = requests.post(USERS_URL, json={"name": name})
    response.raise_for_status()
    user_data = response.json()
    print("✅ User created:", user_data)
    return user_data["id"]

def create_task(user_id, description):
    response = requests.post(TASKS_URL, json={
        "title": description,
        "user_id": user_id
    })
    response.raise_for_status()
    task_data = response.json()
    print("✅ Task created:", task_data)
    return task_data["id"]

def get_tasks():
    response = requests.get(TASKS_URL)
    response.raise_for_status()
    tasks = response.json()
    return tasks

def delete_task(user_id,task_id):
    
    tasks = get_tasks()

    # Buscar la tarea que queremos eliminar
    task_to_delete = next((task for task in tasks if task["id"] == task_id and task["user_id"] == user_id), None)

    if not task_to_delete:
        print(f"❌ Task with ID {task_id} not found or doesn't belong to user {user_id}.")
        return

    # Si la tarea existe y pertenece al usuario, realizar la eliminación
    response = requests.delete(f"{TASKS_URL}/{task_id}", json={"user_id": user_id})
    response.raise_for_status()
    print(f"✅ Task with ID {task_id} deleted successfully.")

def delete_user(user_id):
    user_check = requests.get(f"{USERS_URL}/{user_id}")
    if user_check.status_code != 200:
        print(f"❌ User with ID {user_id} not found.")
        return
    
    # Realizar la solicitud DELETE para eliminar el usuario
    response = requests.delete(f"{USERS_URL}/{user_id}")
    
    if response.status_code == 200:
        print(f"✅ User with ID {user_id} deleted successfully.")
    else:
        print(f"❌ Failed to delete user with ID {user_id}.")

def verify_task_deleted(task_id):
    tasks = get_tasks()
    assert not any(task["id"] == task_id for task in tasks), f"❌ Task with ID {task_id} was not deleted"
    print(f"✅ Task with ID {task_id} has been properly deleted.")

def verify_user_deleted(user_id):
    user_check = requests.get(f"{USERS_URL}/{user_id}")
    assert user_check.status_code == 404, f"❌ User with ID {user_id} was not deleted"
    print(f"✅ User with ID {user_id} has been properly deleted.")

def integration_test():
    delete_task(13,14)
    
    # Step 1: Create user
    user_id = create_user("Camilo")

    # Step 2: Create task for that user
    
    task_id = create_task(user_id, "Prepare presentation")

    # Step 3: Verify that the task is registered and associated with the user
    tasks = get_tasks()
    user_tasks = [t for t in tasks if t["user_id"] == user_id]

    assert any(t["id"] == task_id for t in user_tasks), "❌ The task was not correctly registered"
    print("✅ Test completed: task was successfully registered and linked to the user.")

    # Step 4: Delete task for that user and verify
    delete_task(user_id,task_id)
    verify_task_deleted(task_id)

    # Step 5: Delete user and verify
    delete_user(user_id)
    verify_user_deleted(user_id)


if __name__ == "__main__":
    integration_test()