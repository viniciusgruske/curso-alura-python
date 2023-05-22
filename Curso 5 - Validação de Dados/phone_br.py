import re

class PhoneBR:
    def __init__(self, phone):
        phone = str(phone)
        self._regex_phone = re.compile('^(\\+55)?(\\d{2})(9)?(\\d{4})(\\d{4})$')
        if self._is_valid(phone):
            self.phone = phone
        else:
            raise ValueError('Invalid phone.')

    def __str__(self):
        return self._format()
    
    def _is_valid(self, phone):
        return bool(re.search(self._regex_phone, phone))

    def _format(self):
        regex_search = re.search(self._regex_phone, self.phone)
        char_space = ' '

        if regex_search:        
            if regex_search.group(1) == None: 
                ddi = '+55' 
            else: 
                ddi = regex_search.group(1)
            
            ddd = regex_search.group(2)
            
            if regex_search.group(3) == None:
                ninth_digit = ''
            else:
                ninth_digit = f'{regex_search.group(3)}{char_space}'
            
            first_part = regex_search.group(4)
            
            second_part = regex_search.group(5)

            return f'{ddi} ({ddd}) {ninth_digit}{first_part}-{second_part}'