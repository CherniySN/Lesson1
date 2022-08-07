class Numbers:
    def __init__(self, numbers=None):
        if numbers is not None:
            self.number_list = list(map(int, numbers))
        self.summa = 0
        self.average = 0

    def inspect(self):
        try:
            for x in self.number_list:
                self.summa += x
            self.average = self.summa / 12
            return (print(self.average))
        except:
            print('Something went wrong.')

    def __del__(self):
        self.number_list = None
        print('Прощай мир')


numbers = input('Введите зарплату за каждый месяц через пробел: ').split()
object = Numbers(numbers)
object.inspect()
