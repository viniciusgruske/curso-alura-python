import re

class URLExtractor:
    def __init__(self, url):
        self.url = self.__sanitize(url)
        self.__validate()

    def __eq__(self, other):
        return self.url == other.url

    def __len__(self):
        return len(self.url)
    
    def __str__(self):
        return (f'URL: {self.url}\n'
                f'Tamanho da URL: {len(self)}\n'
                f'Base: {self.url_base}\n'
                f'Parâmetros: {self.url_parameters}')

    def __sanitize(self, url):
        if type(url) == str:
            return url.strip().lower()
        else:
            return ""
    
    def __validate(self):
        url_regex = re.compile('^(http(s)?://)?(www.)?[a-z0-9]+([.][a-z0-9]+){1,}/[a-z0-9]+')
        if not url_regex.match(self.url):
            raise ValueError("Invalid URL")
        
    @property
    def url_base(self):
        symbol_question_index = self.url.find('?')
        return self.url[:symbol_question_index]
    
    @property
    def url_parameters(self):
        question_symbol_index = self.url.find('?')
        return self.url[question_symbol_index + 1:]
    
    def get_parameter_value(self, search_parameter):

        search_parameter_index = self.url_parameters.find(search_parameter) + len(search_parameter) + 1
        symbol_ampersand_index = self.url_parameters.find('&', search_parameter_index)
        if (symbol_ampersand_index == -1):
            return self.url_parameters[search_parameter_index:]
        else:
            return self.url_parameters[search_parameter_index:symbol_ampersand_index]

url_extractor = URLExtractor('https://bytebank.com/cambio?moeda_origem=brl&moeda_destino=brl&quantidade=100')
print(url_extractor)

BRL_TO_USD = 5.5
USD_TO_BRL = 1.0 / BRL_TO_USD

print('Câmbio:')
print(f'U$1.00 = R${BRL_TO_USD:.2f}')
print(f'R$1.00 = U${USD_TO_BRL:.2f}')

source_currency = url_extractor.get_parameter_value('moeda_origem')
destination_currency = url_extractor.get_parameter_value('moeda_destino')
amount = float(url_extractor.get_parameter_value('quantidade'))

if (source_currency == 'brl'):
    if (destination_currency == 'usd'):
        print(f'Valor convertido para USD: U${(amount * BRL_TO_USD):.2f}')
    elif (destination_currency == 'brl'):
        print(f'Valor convertido para BRL: R${amount:.2f}')
elif (source_currency == 'usd'):
    if (destination_currency == 'usd'):
        print(f'Valor convertido para USD: U${(amount):.2f}')
    elif (destination_currency == 'brl'):
        print(f'Valor convertido para BRL: R${amount * USD_TO_BRL:.2f}')
