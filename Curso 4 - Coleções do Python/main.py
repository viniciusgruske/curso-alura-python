# Polimorfismo
class Mãe:
    def ola(self):
        return "Olá"
    def eu_sou(self):
        print(f"{self.ola()}, eu sou a Mãe!")
  
  
class Filha(Mãe):
    def eu_sou(self):
        print(f"{self.ola()}, eu sou a Filha!")

class Neta(Filha):
    def eu_sou(self):
        print(f"{self.ola()}, eu sou a Neta!")

mae = Mãe()
filha = Filha()
neta = Neta()
mae.eu_sou()
filha.eu_sou()
neta.eu_sou()

# Ducktyping
class Pato():
    def nadar(self):
        print("Eu sou um pato, e estou nadando.")
    
    def grasnar(self):
        print("Quack!")

    def voar(self):
        print("Eu sou um pato, e estou voando.")

class Ganso():
    def nadar(self):
        print("Eu sou um ganso, e estou nadando.")
    
    def grasnar(self):
        print("Quá-Quá!")

    def voar(self):
        print("Eu sou um ganso, e estou voando.")

pato = Pato()
ganso = Ganso()

animais = [pato, ganso]

for animal in animais:
    animal.nadar()
    animal.voar()
    animal.grasnar()
