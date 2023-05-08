class BankAccount:
    def __init__(self, account_number, client_name, balance, limit):
        print("Construindo objeto: {}".format(self))
        self.__account_number = account_number
        self.__client_name = client_name
        self.__balance = balance
        self.__limit = limit
        self.__bank_id = BankAccount.bank_id()
###################################################################################################
    @staticmethod
    def bank_id():
        return "001"
###################################################################################################
    @staticmethod
    def banks_id():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}
###################################################################################################
    def bank_statement(self):
        print(f"O saldo do titular {self.__client_name} é de {self.__balance}")
###################################################################################################
    def deposit(self, value):
        self.__balance += value
###################################################################################################
    def withdraw(self, value):
        if (self.__can_withdraw(value)):
            self.__balance -= value
        else:
            print("Saldo insuficiente.")
###################################################################################################
    def transfer(self, value, destination_account):
        self.withdraw(value)
        destination_account.deposit(value)
###################################################################################################
    def __can_withdraw(self, value):
        return value <= (self.__balance + self.__limit)
###################################################################################################
    @property
    def account_number(self):
        return self.__account_number
###################################################################################################
    @property
    def client_name(self):
        return self.__client_name
###################################################################################################
    @property
    def balance(self):
        return self.__balance
###################################################################################################
    @property
    def limit(self):
        return self.__limit
###################################################################################################
    # @property
    # def bank_id(self):
    #     return self.__bank_id
###################################################################################################
    @limit.setter
    def limit(self, value):
        self.__limit = value
