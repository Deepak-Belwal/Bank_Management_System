from account import Account

class Loan:
    @staticmethod
    def apply_for_loan(account: Account, loan_amount):
        if 1000 <= loan_amount <= 99999:
            account.deposit(loan_amount)
            return f"Loan approved! Amount credited: {loan_amount}"
        return "Loan denied! Amount outside permissible range."
