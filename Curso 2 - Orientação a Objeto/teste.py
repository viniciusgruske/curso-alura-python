class Cliente:
    def __init__(self, nome):
        self.__nome = nome
        self.__planeta = self.planeta()

    # Getter: Equivalente a uma função get_nome(self)
    @property
    def nome(self):
        return self.__nome
    
    # Setter: Equivalente a uma função set_nome(self, nome)
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    # Método estático
    @staticmethod
    def planeta():
        return "Terra"

# Criando o objeto:
cliente = Cliente("Nico")

# Chamando o Setter:
cliente.nome = "Marcos"

# Chamando o Getter:
print(cliente.nome)

# Chamando o método estático na classe:
print(Cliente.planeta())

# Chamando o método estático no objeto:
print(cliente.planeta())


class Circle:
    # Atributo Estático
    pi = 3.14
    # Método Estático
    @staticmethod
    def get_pi():
        return 3.14

# Chamando o método estático na classe:
print(Circle.get_pi())

# Chamando o método estático no objeto:
print(Circle.pi)