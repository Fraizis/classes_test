from dataclasses import dataclass


class AccountError(Exception):
    pass


class TransactionError(AccountError):
    pass


@dataclass(frozen=True)
class Transaction:
    amount: float
    description: str


class Account:
    def __init__(self, owner: str, initial_balance: float = 0):
        self.owner = owner
        self._initial_balance = initial_balance
        self._transactions = []

    @property
    def balance(self):
        total = self._initial_balance + sum(trans.amount for trans in self._transactions)
        return total

    def add_transaction(self, transaction: Transaction):
        if not isinstance(transaction, Transaction):
            raise TransactionError('Транзакция невозможна')

        elif self.balance + transaction.amount < 0:
            raise TransactionError('Транзакция невозможна: недостаточно средств.')

        self._transactions.append(transaction)

    @classmethod
    def from_csv(cls, csv_string: str):
        owner, balance = csv_string.split(',')
        return cls(owner=owner, initial_balance=float(balance))

    def __str__(self):
        return f'Счет {self.owner}'

    def __repr__(self):
        return f'Account(owner={self.owner!r}, initial_balance={self._initial_balance})'

    def __len__(self):
        return len(self._transactions)


acc = Account("Иван", 100)
acc.add_transaction(Transaction(50, "Пополнение"))
print(acc.balance)
print(len(acc))
acc.add_transaction(Transaction(-200, "Покупка"))

print()
