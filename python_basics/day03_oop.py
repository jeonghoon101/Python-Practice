class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("입금 금액은 0보다 커야 합니다.")
        else:
            self.balance += amount
    
    def withdraw(self, amount):
        if amount <= 0:
            print("출금 금액은 0보다 커야 합니다.")
        elif amount > self.balance:
            print("잔액이 부족합니다.")
        else:
            self.balance -= amount

    def show_balance(self):
        return f"현재 잔액: {self.balance}원"

account = BankAccount("정훈", 10000)
account.deposit(5000)
account.withdraw(3000)
print(account.show_balance())