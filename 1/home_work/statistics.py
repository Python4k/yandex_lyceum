class MinStat:
    def __init__(self):
        self.firstNum = True
        self.min = None
    
    def add_number(self, num):
        if self.firstNum:
            self.min = num
            self.firstNum = False
        elif self.min > num:
            self.min = num
    
    def result(self):
        return self.min


class MaxStat:
    def __init__(self):
        self.firstNum = True
        self.max = None

    def add_number(self, num):
        if self.firstNum:
            self.max = num
            self.firstNum = False
        elif self.max < num:
            self.max = num
    
    def result(self):
        return self.max
    
    
class AverageStat:
    def __init__(self):
        self.firstNum = True
        self.n = 0
        self.avg = None
    
    def add_number(self, num):
        self.n += 1
        if self.firstNum:
            self.avg = num
            self.firstNum = False
        else:
            self.avg += num
    
    def result(self):
        if self.n:
            return self.avg / self.n
        else: return None
        
    

# Тесты
values = [1, 2, 4, 5]

mins = MinStat()
maxs = MaxStat()
average = AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)

print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))


# Если тип возвращаемого значения должен быть равет типу None
# print(mins.result(), maxs.result(), average.result())