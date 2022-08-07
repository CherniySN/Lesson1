class forest:
    def __init__(self, number_of_visitors=None):
        self.number_of_forest = list(range(30, 36))
        if number_of_visitors is not None:
            self.dictionary_of_visitiors_of_forest = {}
            self.number_of_visitors = list(map(int, number_of_visitors))
            if len(self.number_of_visitors) != len(self.number_of_forest):
                for x in range(len(self.number_of_forest) - len(self.number_of_visitors)):
                    self.number_of_visitors.append(0)
            for vale, i in enumerate(self.number_of_forest):

    def __call__(self):
        for x in self.number_of_forest:
            pass


current_number_of_visitirs = input('Введите количество поситителей: ').split()
s = forest(current_number_of_visitirs)
print(s.number_of_forest)
print(s.number_of_visitors)
