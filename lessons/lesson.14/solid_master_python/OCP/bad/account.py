class AccountType:
    CHECKING = "checking"
    SAVINGS = "savings"

class DebitAccount:
    def debit(self, amount: float, account: str, account_type: str):
        if account_type == AccountType.CHECKING:
            # Debit from checking account
            print(f"Debiting {amount} from checking account {account}")

        if account_type == AccountType.SAVINGS:
            # Validate account anniversary
            # Debit from savings account
            print(f"Debiting {amount} from savings account {account}, validating anniversary date")