class Point:
    def __init__(p, x1, y1):
        p.x = x1
        p.y = y1

    def inp(p):
        p.x = int(input())
        p.y = int(input())

    def show(p):
        print("(", p.x, ",", p.y, ')', sep='')

    def move(p, x1, x2):
        p.x += x1
        p.y += x2

    def dist(p1, p2):
        d = ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5
        print(d)


a = Point(1, 3)
b = Point(0, 0)
b.inp()
a.show()
b.show()
a.move(4, 6)
a.show()
a.dist(b)
