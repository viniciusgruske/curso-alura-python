import re

url = 'https://www.google.com.br/'
regex = re.compile('.com.br/')

regex_search = regex.search(url)
regex_match = regex.match(url)

if regex_search:
    url_regex = regex_search.group()
    print(url_regex)
else:
    print(False)

if regex_match:
    url_regex = regex_match.group()
    print(url_regex)
else:
    print(False)