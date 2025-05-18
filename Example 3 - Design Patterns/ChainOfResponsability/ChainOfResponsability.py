# Clase base Handler
class Handler:
    def __init__(self, next_handler=None):
        self.next = next_handler

    def handle(self, data):
        if self.next:
            self.next.handle(data)

# Handler para verificar si existe el nombre de usuario
class UsernameExistsHandler(Handler):
    def handle(self, data):
        if not data.get("username"):
            print("Error: Falta el nombre de usuario.")
        else:
            super().handle(data)

# Handler para verificar longitud del nombre de usuario
class UsernameLengthHandler(Handler):
    def handle(self, data):
        if len(data.get("username", "")) < 4:
            print("Error: El nombre de usuario es muy corto.")
        else:
            super().handle(data)

# Handler para verificar si el email está presente
class EmailExistsHandler(Handler):
    def handle(self, data):
        if not data.get("email"):
            print("Error: Falta el email.")
        else:
            super().handle(data)

# Handler para verificar que el email tiene formato válido (muy básico)
class EmailFormatHandler(Handler):
    def handle(self, data):
        email = data.get("email", "")
        if "@" not in email or "." not in email:
            print("Error: El formato del email es inválido.")
        else:
            super().handle(data)

# Handler final: si todo fue bien
class SuccessHandler(Handler):
    def handle(self, data):
        print("✅ Validación exitosa.")

# Armar la cadena de responsabilidad
handler_chain = UsernameExistsHandler(
    UsernameLengthHandler(
        EmailExistsHandler(
            EmailFormatHandler(
                SuccessHandler()
            )
        )
    )
)

# Prueba 1: con errores
user_data1 = {"username": "bob", "email": ""}
print("=== Prueba 1 ===")
handler_chain.handle(user_data1)

# Prueba 2: exitosa
user_data2 = {"username": "roberto", "email": "roberto@mail.com"}
print("\n=== Prueba 2 ===")
handler_chain.handle(user_data2)