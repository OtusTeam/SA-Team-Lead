class PaymentMethod:
    def process_payment(self, amount):
        raise NotImplementedError("This method should be overridden in subclasses")

class Refundable:
    def refund_payment(self, amount):
        raise NotImplementedError("This method should be overridden in subclasses")

class CreditCardPayment(PaymentMethod, Refundable):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

    def refund_payment(self, amount):
        print(f"Refunding credit card payment of ${amount}")

class PayPalPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

# Теперь можно проверять, поддерживает ли платежная система возврат
def handle_payment(payment_method: PaymentMethod, amount):
    payment_method.process_payment(amount)
    if isinstance(payment_method, Refundable):
        payment_method.refund_payment(amount)

credit_card_payment = CreditCardPayment()
paypal_payment = PayPalPayment()

handle_payment(credit_card_payment, 100)  # Всё ок
handle_payment(paypal_payment, 50)  # Возврат не будет выполнен, но ошибка не возникнет
