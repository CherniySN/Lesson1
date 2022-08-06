class Numbers:
    def __int__(self):
        self.isFlag = True

    def __call__(self, numbers):
        self.number_list = list(map(int, numbers))
        for x in self.number_list:
            if x % 2 == 0:
                if x > 0:
                    self.isFlag = True
                else:
                    self.isFlag = False
            else:
                self.isFlag = False
        if self.isFlag:
            return (print(x, 'Число четное и положительное.'))
        else:
            return (print(x, 'Число не подходит'))


numbers = input('Введите числа через пробел: ').split()
object = Numbers()
object(numbers)
