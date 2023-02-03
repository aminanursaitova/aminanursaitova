a = int(input())
m = 1
k = 1
b = -1
while b != 0:
    b = int(input())
    if a == b:
        k += 1
    elif k > m:
        m = k
        k = 1
    else:
        k = 1
    a = b
print(m)