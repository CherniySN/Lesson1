class forest:
    def __init__(self, number_of_visitors=None):
        if number_of_visitors is not None:
            self.number_of_visitors = list(map(int, number_of_visitors))
        self.number_of_forest = list(range(30, 36))

    def __call__(self):
        for x in self.number_of_forest:
            pass


current_number_of_visitirs = input('Введите количество поситителей: ').split()
s = forest(current_number_of_visitirs)
print(s.number_of_visitors)
