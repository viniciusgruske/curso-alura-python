from validate_docbr import CPF,CNPJ

class Document:
    @staticmethod
    def new(document):
        document = str(document)
        if len(document) == 11:
            return DocumentCPF(document)
        if len(document) == 14:
            return DocumentCNPJ(document)
        raise ValueError('Unable to determine document type.')
    
class DocumentCPF:
    def __init__(self, document):
        if self._is_valid(document):
            self.cpf = document
        else:
            raise ValueError('Invalid CPF.')
        
    def __str__(self):
        return self._format()

    def _is_valid(self, document):
        return CPF().validate(document)

    def _format(self):
        return CPF().mask(self.cpf)

class DocumentCNPJ:
    def __init__(self, document):
        if self._is_valid(document):
            self.cnpj = document
        else:
            raise ValueError('Invalid CNPJ.')
        
    def __str__(self):
        return self._format()

    def _is_valid(self, document):
        return CNPJ().validate(document)

    def _format(self):
        return CNPJ().mask(self.cnpj)