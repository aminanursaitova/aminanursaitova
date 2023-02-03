n = 0
m = 1
k = 0
a = int(input())
while n != a:
    if n > a:
        k = -1
        break
    k += 1
    z = m
    m += n
    n = z
print(k)



