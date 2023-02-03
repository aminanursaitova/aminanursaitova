s=input()
x=s.find('h')
y=s.rfind('h')
l=s[x+1:y]
print(s[:x+1]+l.replace('h','H')+s[y:])
