class Car:
    def __init__(x, fl, str1, str2):
        x.engine = fl
        x.mark = str1
        x.color = str2

    def printinfo(x):
        print("Your Car's parameters:", x.engine, x.mark, x.color)


class Toyota(Car):
    def __init__(x, fl, str1, str2):
        super().__init__(fl, str1, str2)
        x.country = "Japan"

    def printinfo(x):
        print("Your Toyota's parameters:", x.engine, x.mark, x.color, x.country)

    def getter(x):
        print("Your Toyota's price:", x.price)

    def setter(x, a):
        x.price = a


class Camry(Toyota):
    def __init__(x, fl, str1, str2):
        super().__init__(fl, str1, str2)
        x.wheels = 4

    def printinfo(x):
        print("Your Camry's parameters:", x.engine, x.mark, x.color, x.country, x.wheels)

v = Toyota(4.5, "toyoyo", "magenta")
a = 15
v.setter(a)
v.printinfo()
v.getter()
s = Camry(3.5, "tttt", "cyan")
s.printinfo()