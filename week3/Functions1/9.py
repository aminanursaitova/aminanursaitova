import math

def vol(r):
    return math.pi * 4 * (r ** 3) / 3

r = int(input())
print(vol(r))