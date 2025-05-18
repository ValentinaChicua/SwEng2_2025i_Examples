def process_payment(method, amount):
    if method == "paypal":
        print(f"Pagando ${amount} con PayPal.")
    elif method == "credit_card":
        print(f"Pagando ${amount} con tarjeta de crédito.")
    else:
        print("Método de pago no soportado.")

# Uso
process_payment("paypal", 100)
process_payment("credit_card", 200)



