n = 0
m = 1
k = 0
a = int(input())
while (k < a):
    k += 1
    z = m
    m += n
    n = z
print(n)