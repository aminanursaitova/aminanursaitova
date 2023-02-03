a = 1
m = 0
n = 0
a = int(input())
while(a != 0):
    if a > m:
        n = m
        m = a
    elif a > n:
        n = a
    a = int(input())
print(n)
