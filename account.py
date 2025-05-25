class Account:
    def __init__(self, id_number, ph_number, name, father_name, pin, balance):
        self.id_number = id_number
        self.ph_number = ph_number
        self.name = name
        self.father_name = father_name
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposit successful! New balance: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance!"
        self.balance -= amount
        return f"Withdrawal successful! New balance: {self.balance}"
