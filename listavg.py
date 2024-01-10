class ListAverage:
    def __init__(self, lst):
        self.lst = lst.copy()
        self.total_sum = sum(lst)

    def add(self, num):
        self.lst.append(num)
        self.total_sum += num

    def compute_avg(self):
        total = 0
        for num in self.lst:
            total += num
        return total / len(self.lst)

    def compute_avg_faster(self):
        average = self.total_sum / len(self.lst)
        return float(f'{average:.1f}')
    
average = ListAverage([1, 3, 5, 7, 9, 11, 13])
print(average.compute_avg())
print(average.compute_avg_faster())
average.add(4)
average.add(5)
print(average.compute_avg_faster())
print(type(average))

