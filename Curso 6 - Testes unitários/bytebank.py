from datetime import date

class Funcionario:
    def __init__(self, name, birth_day, salary):
        self._name = name
        self._birth_day = birth_day
        self._salary = salary

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary
    
    @property
    def last_name(self):
        last_name = self.name.strip().split(' ')
        return last_name[-1]

    @property
    def age(self):
        full_birth_day = self._birth_day.split('/')
        year_birth_day = full_birth_day[2]
        actual_year = date.today().year
        return actual_year - int(year_birth_day)

    def calculate_bonus(self):
        value = self._salary * 0.1
        if self.salary > 1000:
            raise Exception('Salary is too high to calculate a bonus.')
        return value
    
    def _is_director(self, last_name):
        directors_last_name = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
        return self._salary >= 100000 and last_name in directors_last_name
    
    def salary_decrease(self):
        if self._is_director(self.last_name):
            self._salary *= 0.9

    def __str__(self):
        return f'Funcionario({self._name}, {self._birth_day}, {self._salary})'