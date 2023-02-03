m = 0
a = int(input())
while(a != 0):
    if a > m:
        k = 1
        m = a
    elif a == m:
        k += 1
    a = int(input())
print(k)
