import random
import string
from abc import ABC, abstractmethod


class DebitoConta(ABC):
    def __init__(self):
        self.numero_transacao = ""

    @abstractmethod
    def debitar(self, valor: float, conta: str) -> str:
        pass

    def formatar_transacao(self) -> str:
        chars = string.ascii_uppercase + string.digits
        self.numero_transacao = "".join(random.choices(chars, k=15))
        return self.numero_transacao


class DebitoContaCorrente(DebitoConta):
    def debitar(self, valor: float, conta: str) -> str:
        # Debita Conta Corrente
        return self.formatar_transacao()


class DebitoContaInvestimento(DebitoConta):
    def debitar(self, valor: float, conta: str) -> str:
        # Debita Conta Investimento
        # Isentar Taxas
        return self.formatar_transacao()


class DebitoContaPoupanca(DebitoConta):
    def debitar(self, valor: float, conta: str) -> str:
        # Valida Aniversário da Conta
        # Debita Conta Poupança
        return self.formatar_transacao()
