# from Date import Date
# date = Date(21,11,2007)
# date.format()

from BankAccount import BankAccount
print(BankAccount.bank_id())

account1 = BankAccount(123, "Nico", 50.0, 1000.0)
account2 = BankAccount(321, "Marco", 100.0, 1000.0)

print(account1.bank_id())
print(account2.bank_id())

account1.withdraw(2000)
account2.transfer(2000, account1)

account1.bank_statement()
account2.bank_statement()