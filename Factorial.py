"""
Мы всё ближе и ближе подбираемся к серьёзной математике. Одна из классических задач —
задача на нахождение факториала числа. И в будущем мы с ней ещё встретимся.

Дано натуральное число n. Напишите программу, которая находит n! (n-факториал).
"""


class Factorial:
    def __init__(self, number=0):
        if number != 0:
            self.number = number
        self.factor = 1

    def resh(self):
        for x in range(1, self.number + 1):
            self.factor = x * self.factor
        return self.factor

    def __del__(self):
        print('Прощай мир!')


numbre = int(input('Введите число для расчета факториала: '))
number_factorial = Factorial(numbre)
print(number_factorial.resh())
