numbers = [int(k) for k in input().split()]
prime = list(filter(lambda x: all(x % n != 0 for n in range (2, int(x**0.5) + 1)), numbers))
print(prime)