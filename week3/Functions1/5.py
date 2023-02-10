a = ""

def ps(s, a):
    if (len(s) == 0):
        print(a, end="  ")
        return
    for i in range(len(s)):
        c = s[i]
        l = s[0:i]
        r = s[i + 1:]
        d = l + r
        ps(d, a + c)

s = input()
ps(s, a)
