from bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:
    def test__Funcionario__idade(self):
        input = '27/02/1996'
        output = 27
        
        test_employee = Funcionario('Teste', '27/02/1996', 2650)
        result = test_employee.age

        assert result == output

    def test___when___salary_decrease___receive_100k___must_return___90k(self):
        input = 100000
        output = 90000

        test_employee = Funcionario('Paulo Bragança', '27/02/1996', input)
        test_employee.salary_decrease()
        result = test_employee.salary

        assert result == output

    @mark.calculate_bonus
    def test___when___calculate_bonus___receive_1k___must_return___100(self):
        input = 1000
        output = 100

        test_employee = Funcionario('Teste', '27/02/1996', input)
        result = test_employee.calculate_bonus()

        assert result == output

    @mark.calculate_bonus
    def test___when___calculate_bonus___receive_2k___must_return___exception(self):
        with pytest.raises(Exception):
            input = 2000

            test_employee = Funcionario('Teste', '27/02/1996', input)
            result = test_employee.calculate_bonus()

            assert result

    # def test___str___(self):
    #     name, birth_day, salary = 'Teste', '27/02/1996', 1000
    #     output = f"Funcionario({name}, {birth_day}, {salary})"

    #     result = Funcionario(name, birth_day, salary)

    #     assert str(result) == output