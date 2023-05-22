from document import Document
from phone_br import PhoneBR

cpf = Document().new('85540609034')
cnpj = Document().new('21967557000176')
print(cpf)
print(cnpj)

phone = PhoneBR('5133741442')
cell_phone = PhoneBR('51981357480')
print(phone)
print(cell_phone)

