"""Напишите программу, которая считывает с клавиатуры два числа a и b,
считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a; b], кратных числу 3.
"""


class Kratnost:
    def __init__(self, numbers=None):
        if numbers != None:
            self.numbers = list(map(int, numbers))

    def rashchet(self):
        for x in range(self.numbers[0], self.numbers[1]):
