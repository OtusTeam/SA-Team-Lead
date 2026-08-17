import random
import string
from abc import ABC, abstractmethod


class AccountDebit(ABC):
    def __init__(self):
        self.transaction_number = ""

    @abstractmethod
    def debit(self, amount: float, account: str) -> str:
        pass

    def generate_transaction_number(self) -> str:
        chars = string.ascii_uppercase + string.digits
        self.transaction_number = "".join(random.choices(chars, k=15))
        return self.transaction_number


class CheckingAccountDebit(AccountDebit):
    def debit(self, amount: float, account: str) -> str:
        # Debit checking account
        return self.generate_transaction_number()


class InvestmentAccountDebit(AccountDebit):
    def debit(self, amount: float, account: str) -> str:
        # Debit investment account
        # Apply tax exemption rules
        return self.generate_transaction_number()


class SavingsAccountDebit(AccountDebit):
    def debit(self, amount: float, account: str) -> str:
        # Validate account anniversary date
        # Debit savings account
        return self.generate_transaction_number()