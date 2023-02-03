z = -1
i = -1
a = int(input())
while(a != 0):
    i += 1
    if a > z:
        z = a
        k = i
    a = int(input())
print(k)