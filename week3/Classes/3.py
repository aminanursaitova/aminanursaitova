class Shape:
    def __init__(x):
        x.l = 0
        x.w = 0

    def inp(x):
        x.l = int(input())
        x.w = int(input())

    def Area(x):
        x.a = 0
        print(x.a)


class Rectangle(Shape):
    def __init__(x):
        super().__init__()

    def Area(x):
        x.a = x.l * x.w
        print(x.a)


f = Rectangle()
f.inp()
f.Area()
