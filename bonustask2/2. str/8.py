s=input()
x=s.find('h')
y=s.rfind('h')
print(s[:x+1]+s[y-1:x:-1]+s[y:])
