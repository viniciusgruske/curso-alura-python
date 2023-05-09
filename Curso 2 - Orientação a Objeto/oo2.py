class Production:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def give_like(self):
        self._likes += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name.title()

    def __str__(self):
        return (f'Filme: {self.name}\n'
                f'Ano: {self.year}\n'
                f'Likes: {self.likes}')

class Film(Production):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return (f'Filme: {self.name}\n'
                f'Ano: {self.year}\n'
                f'Duração: {self.duration}\n'
                f'Likes: {self.likes}')
        
class Serie(Production):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return (f'Filme: {self.name}\n'
                f'Ano: {self.year}\n'
                f'Temporadas: {self.seasons}\n'
                f'Likes: {self.likes}')

class Playlist:
    def __init__(self, name, productions):
        self.name = name
        self._productions = productions
    
    def __getitem__(self, index):
        return self._productions[index]
    
    @property
    def productions(self):
        return self._productions    

vingadores = Film('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)

vingadores.give_like()
atlanta.give_like()
atlanta.give_like()

productions = [vingadores, atlanta]
playlist = Playlist('playlist1', productions)

for index in playlist:
    print(index)
    print()