"""Напишите программу, которая считывает с клавиатуры два числа a и b,
считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a; b], кратных числу 3.
"""


class Kratnost:
    def __init__(self, numbers=None):
        if numbers != None:
            self.numbers = list(map(int, numbers))
        self.totalsum = 0
        self.i = 0
        self.average = 0

    def rashchet(self):
        for x in range(self.numbers[0], self.numbers[1] + 1):
            if x % 3 == 0:
                self.totalsum += x
                self.i += 1
        self.average = self.totalsum / self.i
        return (self.average)


ob = input('Введите два числа ').split()
a = Kratnost(ob)
print(a.rashchet())
