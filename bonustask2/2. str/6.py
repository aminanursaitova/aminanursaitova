s=input()
x=s.find("f")
if s.count('f')==1:
    print(-1)
elif s.count('f')==0:
    print(-2)
else:
    print(s.find('f', x+1))
