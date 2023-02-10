class Shape:
    def __init__(x):
        x.l = 0
        x.w = 0

    def inp(x):
        x.l, x.w = int(input())

    def Area(x):
        x.a = 0
        print(x.a)

class Square(Shape):
    def __init__(x):
        x.l = 0

    def inp(x):
        x.l = int(input())

    def Area(x):
        x.a = x.l * x.l
        print(x.a)

f = Square()
f.inp()
f.Area()