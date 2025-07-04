import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def abrir_frontend(driver):
    # Opens the frontend application in the browser
    driver.get("http://localhost:5000")
    time.sleep(2)  # Give the page time to load

def crear_usuario(driver, wait):
    # Fills out the user creation form and submits it
    # Then retrieves and returns the newly created user ID
    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys("Ana")
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[contains(text(), 'Crear Usuario')]").click()
    time.sleep(2)

    user_result = driver.find_element(By.ID, "user-result").text
    print("Resultado usuario:", user_result)
    assert "Usuario creado con ID" in user_result
    user_id = ''.join(filter(str.isdigit, user_result))  # Extract numeric ID from result
    return user_id

def crear_tarea(driver, wait, user_id):
    # Fills out the task creation form with a task and user ID, then submits it
    # Waits until the confirmation text appears and asserts the result
    task_input = driver.find_element(By.ID, "task")
    task_input.send_keys("Terminar laboratorio")
    time.sleep(1)

    userid_input = driver.find_element(By.ID, "userid")
    userid_input.send_keys(user_id)
    userid_input.send_keys('\t')  # Force focus out of the input to trigger validation
    time.sleep(1)

    crear_tarea_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Crear Tarea']"))
    )
    crear_tarea_btn.click()
    time.sleep(2)

    wait.until(
        EC.text_to_be_present_in_element((By.ID, "task-result"), "Tarea creada con ID")
    )
    task_result = driver.find_element(By.ID, "task-result")
    print("Texto en task_result:", task_result.text)
    assert "Tarea creada con ID" in task_result.text

def ver_tareas(driver):
    # Clicks the button to refresh the task list and verifies the new task appears
    driver.find_element(By.XPATH, "//button[contains(text(), 'Actualizar lista de tareas')]").click()
    time.sleep(2)

    tasks = driver.find_element(By.ID, "tasks").text
    print("Tareas:", tasks)
    assert "Terminar laboratorio" in tasks

def eliminar_tarea(driver, user_id):
    task_list = driver.find_elements(By.CSS_SELECTOR, "#tasks li")
    assert task_list, "No hay tareas para eliminar"

    # Extraer ID de la última tarea
    last_task = task_list[-1].text
    task_id = ''.join(filter(str.isdigit, last_task.split("ID: ")[1].split(",")[0]))

    # Limpiar y llenar inputs
    delete_id_input = driver.find_element(By.ID, "delete-task-id")
    delete_user_input = driver.find_element(By.ID, "delete-task-user-id")
    delete_id_input.clear()
    delete_user_input.clear()
    delete_id_input.send_keys(task_id)
    delete_user_input.send_keys(user_id)

    # Hacer clic en botón eliminar
    driver.find_element(By.XPATH, "//button[contains(text(), 'Eliminar Tarea')]").click()

    # Esperar hasta que el mensaje aparezca
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "delete-task-result"), "eliminada")
    )

    # Verificar el mensaje
    result = driver.find_element(By.ID, "delete-task-result").text
    print("Texto recibido al eliminar tarea:", repr(result))
    assert "eliminada" in result.lower()


def eliminar_usuario(driver, user_id):
    driver.find_element(By.ID, "delete-user-id").send_keys(user_id)
    driver.find_element(By.XPATH, "//button[contains(text(), 'Eliminar Usuario')]").click()
    time.sleep(2)

    result = driver.find_element(By.ID, "delete-user-result").text
    print("Eliminar usuario:", result)
    assert f"Usuario con ID {user_id} eliminado correctamente" in result

def main():
    # Main test runner that initializes the browser and runs the full E2E flow
    options = Options()
    # options.add_argument('--headless')  # Uncomment for headless mode
    driver = webdriver.Chrome(options=options)

    try:
        wait = WebDriverWait(driver, 10)
        abrir_frontend(driver)
        user_id = crear_usuario(driver, wait)
        crear_tarea(driver, wait, user_id)
        ver_tareas(driver)

        # cleanup
        eliminar_tarea(driver, user_id)
        eliminar_usuario(driver, user_id)

        #verify
        ver_tareas(driver)

        time.sleep(3)  # Final delay to observe results if not running headless
    finally:
        driver.quit()  # Always close the browser at the end

if __name__ == "__main__":
    main()
