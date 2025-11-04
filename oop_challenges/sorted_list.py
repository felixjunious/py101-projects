import bisect as b

# [2,3,5,5,7,7,7,8,8,9]

class SortedList:
    def __init__(self):
        self.lst = []

    def add(self, value):
        b.insort_left(self.lst, value)

    def remove(self, value):
        self.lst.remove(value)

    def search(self, key):
        return self.lst.index(key)

    def insert_pos(self, value):
        return b.bisect_left(self.lst, value)

    def display(self):
        print(self.lst)

sl = SortedList()
sl.add(10)
sl.add(5)
sl.add(7)
sl.display()