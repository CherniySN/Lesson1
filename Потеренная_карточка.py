"""
Для настольной игры используются карточки с номерами от 1 до N. Одна карточка потерялась.
Напишите программу, которая поможет найти потерянную карточку, если номера оставшихся известны.
Найдите её, зная номера оставшихся карточек.

Введите число карточек — N.

Затем последовательно введите N – 1 номера оставшихся карточек.
"""


class Kartochkf:

    def __init__(self, numbers_of_kartochek, cifri_of_kertochek):
        if numbers_of_kartochek is not None:
            self.numbers_of_kartochek = numbers_of_kartochek
        if cifri_of_kertochek is not None:
            self.cifri_of_kertochek = list(map(int, cifri_of_kertochek))

    def poisk_kartochki(self):
        try:
            swapped = True
            while swapped:
                for i in range(len(self.cifri_of_kertochek) - 1):
                    if self.cifri_of_kertochek[i] > self.cifri_of_kertochek[i + 1]:
                        self.cifri_of_kertochek[i], self.cifri_of_kertochek[i + 1] = self.cifri_of_kertochek[i + 1], \
                                                                                     self.cifri_of_kertochek[i]
                        swapped = True

            swapped2 = True
            while swapped2:
                for i in range(len(self.cifri_of_kertochek) - 1):
                    if self.cifri_of_kertochek[i] == self.cifri_of_kertochek[i + 1]:
                        swapped2 = True
                    else:
                        print('Потерянная карточка с номером: ', self.cifri_of_kertochek[i + 1])
                        swapped2 = False
        except:
            print('Вы ввели что-то не то.')


numebrs_kartochek = int(input('Введите число карточек: '))
cifri_kartochek = input('Введите номер карточек: ').split()

kartochki = Kartochkf(numbers_of_kartochek=numebrs_kartochek, cifri_of_kertochek=cifri_kartochek)
kartochki.poisk_kartochki()
