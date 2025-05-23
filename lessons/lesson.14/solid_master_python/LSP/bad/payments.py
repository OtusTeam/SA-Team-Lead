class PaymentMethod:
    def process_payment(self, amount):
        raise NotImplementedError("This method should be overridden in subclasses")

    def refund_payment(self, amount):
        raise NotImplementedError("Refund is not supported for PayPal payments")

class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

    def refund_payment(self, amount):
        print(f"Refunding credit card payment of ${amount}")

class PayPalPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

    # Нарушение LSP: у PayPal нет операции возврата, и метод refund_payment не будет работать для этого класса
    def refund_payment(self, amount):
        raise NotImplementedError("Refund is not supported for PayPal payments")


def handle_payment(payment_method: PaymentMethod, amount):
    payment_method.process_payment(amount)
    # Ожидаем, что метод возврата будет доступен для всех типов платёжных систем
    payment_method.refund_payment(amount)

credit_card_payment = CreditCardPayment()
paypal_payment = PayPalPayment()

# Это сработает, потому что и CreditCardPayment, и PayPalPayment имеют метод refund_payment
handle_payment(credit_card_payment, 100)

# Это вызовет ошибку, потому что PayPalPayment не поддерживает возвраты
handle_payment(paypal_payment, 50)
