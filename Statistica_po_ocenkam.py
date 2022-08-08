"""
В классе N человек. Каждый из них получил за урок по информатике
оценку: 3, 4 или 5, двоек сегодня не было. Напишите программу,
которая получает список оценок — N чисел — и выводит на экран сообщение о том,
кого сегодня больше: отличников, хорошистов или троечников.

Замечание: можно предположить, что количество отличников, хорошистов, троечников различно.
"""


class RashchetKolOcenok:
    def __init__(self, ocenki_za_den=None):
        if ocenki_za_den != None:
            self.ocenki_za_den = list(map(int, ocenki_za_den))
        self.otl = 0
        self.hor = 0
        self.tri = 0

    def podshet(self):
        for x in self.ocenki_za_den:
            if x == 5:
                self.otl += 1
            elif x == 4:
                self.hor += 1
            else:
                self.tri += 1
        if self.otl > self.hor & self.otl > self.tri:
            print('Оценок 5 больше всего', self.otl)
        elif self.hor > self.otl & self.hor > self.tri:
            print('Оценок 4 больше всего', self.hor)
        else:
            print('Больше всего троек', self.tri)


ocenki = input('Введите оценки за день: ').split()
day = RashchetKolOcenok(ocenki)
day.podshet()
