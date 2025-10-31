class Rectangle:
    count = 0

    def __init__(self,l=1,b=1):
        self.length = l
        self.breadth = b
        Rectangle.count += 1

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self,l):
        if l >= 0:
            self._length = l
        else:
            self._length = 1

    @property
    def breadth(self):
        return self._breadth

    @breadth.setter
    def breadth(self,b):
        if b >= 0:
            self._breadth = b
        else:
            self._breadth = 1

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def calc_area(length, breadth):
        return length * breadth


if __name__ == '__main__':
    r1 = Rectangle(15,8)
    r2 = Rectangle(7,4)
    r3 = Rectangle()
    print(Rectangle.get_count())

    print(r1.length)
    r1.length = -9
    print(r1.length)

    print(Rectangle.calc_area(10,7))