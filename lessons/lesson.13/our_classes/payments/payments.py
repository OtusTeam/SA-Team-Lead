class Bank:

    def __init__(self, name):
        self.name = name

class Payment:
    '''
    сумма
    дата
    банк получателя, отправителя
    валюта
    фио плательщика
    фио получателя
    получатель
    плательщик
    номер
    назначение
    комментарий
    вид платежа
    '''

    '''
    отозвать
    создать 
    отменить
    скорректировать (изменить)
    hold задержать
    изменить банк
    сделать копию
    сохранить
    создать шаблон платежа
    '''

    def __init__(self, value, date, bank, sender_name, number, comment=""):
        self.value = value
        self.date = date
        self.bank = bank
        self.sender_name = sender_name
        self.number = number
        self.comment = comment
        self.status = 'active'

    def cancel(self):
        self.status = 'canceled'


new_payment = Payment(
    200,
    '01.02.2003',
    'T-Bank',
    'Leonid Orlov',
    2344,
)

alpha_bank = Bank('Альфа-Банк')

other_payment = Payment(
    500,
    '01.02.2003',
    alpha_bank,
    'Leonid Orlov',
    234567,
)

print(new_payment.value)
print(new_payment.status == 'active')

new_payment.cancel()

print(new_payment.status)

