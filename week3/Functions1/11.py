def palindrome(s):
    if s == s.reverse():
        return True
    return False

s = input()
print(palindrome(s))