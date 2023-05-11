url = 'https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'
# print(url)

index_question_symbol = url.find('?')

url_base = url[:index_question_symbol]
url_parameters = url[index_question_symbol + 1:]
# print(url_base)
# print(url_parameters)

search_parameter = 'quantidade'
search_parameter_index = url_parameters.find(search_parameter) + len(search_parameter) + 1
index_ampersand_symbol = url_parameters.find('&', search_parameter_index)
if (index_ampersand_symbol == -1):
    search_parameter_value = url_parameters[search_parameter_index:]
else:
    search_parameter_value = url_parameters[search_parameter_index:index_ampersand_symbol]

print(search_parameter_value)
