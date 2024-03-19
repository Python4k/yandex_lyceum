class AmericanDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def set_year(self, year):
        self.year = year

    def set_month(self, month):
        self.month = month

    def set_day(self, day):
        self.day = day

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month
    
    def get_day(self):
        return self.day

    def format(self):
        if self.day < 10 and self.month >= 10:
            return f"{self.month}.{'0'+str(self.day)}.{self.year}"
        if self.month < 10 and self.day >= 10:
            return f"{'0' + str(self.month)}.{self.day}.{self.year}"
        if self.day < 10 and self.month < 10:
            return f"{'0' + str(self.month)}.{'0'+str(self.day)}.{self.year}"
        else:
            return f"{self.month}.{self.day}.{self.year}"


class EuropeanDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def set_year(self, year):
        self.year = year

    def set_month(self, month):
        self.month = month

    def set_day(self, day):
        self.day = day

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def format(self):
        if self.day < 10 and self.month >= 10:
            return f"{'0' + str(self.day)}.{self.month}.{self.year}"
        if self.month < 10 and self.day >= 10:
            return f"{self.day}.{'0'+str(self.month)}.{self.year}"
        if self.day < 10 and self.month < 10:
            return f"{'0' + str(self.day)}.{'0'+str(self.month)}.{self.year}"
        else:
            return f"{self.day}.{self.month}.{self.year}"


# Тесты из задания
american = AmericanDate(2000, 4, 10)
european = EuropeanDate(2000, 4, 10)
print(american.format())
print(european.format())
