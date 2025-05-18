class PaypalPayment:
    def pay(self, amount):
        print(f"Pagando ${amount} con PayPal.")

class CreditCardPayment:
    def pay(self, amount):
        print(f"Pagando ${amount} con tarjeta de crédito.")

class PaymentContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_payment(self, amount):
        self.strategy.pay(amount)

# Uso
payment = PaymentContext(PaypalPayment())
payment.execute_payment(100)

payment.strategy = CreditCardPayment()
payment.execute_payment(200)


