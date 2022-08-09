"""
Пока бухгалтер считала среднюю зарплату сотрудников, ей стало интересно,
а не зря ли она работает столько времени на одном месте? Ей захотелось
узнать, увеличивается ли её зарплата с каждым месяцем или нет.

Пользователь вводит десять чисел. Напишите программу, которая проверяет,
 упорядочены ли они по возрастанию.
"""


class Zarplata:
    def __init__(self, numbers=None):
        if numbers is not None:
            self.numbers = list(map(int, numbers))
            self.numbers_original = self.numbers.copy()

    def podschet(self):
        Zarplata.bubble_sort(self)
        if self.numbers == self.numbers_original:
            print('Введенные значение указаны по возрастанию')
        else:
            print('Вееденные значения указаны не по возрастанию')

    def bubble_sort(self):
        # Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(self.numbers) - 1):
                if self.numbers[i] > self.numbers[i + 1]:
                    # Меняем элементы
                    self.numbers[i], self.numbers[i + 1] = self.numbers[i + 1], self.numbers[i]
                    # Устанавливаем swapped в True для следующей итерации
                    swapped = True


zarplata = input('Введите числа через пробел: ').split()
classA = Zarplata(numbers=zarplata)
classA.podschet()
