i = 0
a = int(input())
z = a
while(a != 0):
    a = int(input())
    if a > z:
        i += 1
        
    z = a
print(i)