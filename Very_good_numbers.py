"""
Напишите программу, которая находит и выводит все двузначные числа,
которые равны утроенному произведению своих цифр. К таким относятся, например, 15 и 24.
"""


class NaidemChislo:
    def __init__(self, chislo=None):
        if chislo is not None:
            self.chislo = str(chislo)

    def naidem_chislo(self):
        if (int(self.chislo[0]) * int(self.chislo[1]) * 3) == int(self.chislo):
            print('Это замечательное число.')


numbers = NaidemChislo(15)
numbers.naidem_chislo()
