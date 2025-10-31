import math

class Circle:
    def __init__(self,r=1.0):
        self.radius = r

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        if r > 0:
            self._radius = r
        else:
            self._radius = 1

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':

    radius = float(input('Enter Radius : '))

    c = Circle(radius)
    print(f'Area: {c.area():.2f}')
    print(f'Perimeter: {c.perimeter():.2f}')



