def validate_user(data):
    if not data.get("username"):
        print("Error: Falta el nombre de usuario.")
        return
    if len(data["username"]) < 4:
        print("Error: El nombre de usuario es muy corto.")
        return
    if not data.get("email"):
        print("Error: Falta el email.")
        return
    print("Validación exitosa.")

# Uso
user_data = {"username": "bob", "email": ""}
validate_user(user_data)


