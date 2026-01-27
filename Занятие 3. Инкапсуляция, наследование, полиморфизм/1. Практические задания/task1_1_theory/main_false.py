# TODO скопириуйте и запустите здесь необходимый код
class BadBankAccount:
    def __init__(self, account_number: str, balance: float):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Недостаточно средств")








if __name__ == "__main__":
    # -------- Пример плохой инкапсуляции --------------

    # Создаем объект банковского счета
    account = BadBankAccount("123456", 1000.0)

    # Плохая практика: Прямое изменение баланса извне
    account.balance = 5000.0  # Баланс можно изменить без проверок

    print(account.balance)  # 5000.0, что может быть ошибкой