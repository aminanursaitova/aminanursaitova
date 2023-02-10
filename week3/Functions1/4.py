def filter_prime(a):
    prime = list(filter(lambda x: all(x % n != 0 for n in range (2, int(x**0.5) + 1)), a))
    return prime

a = [int(k) for k in input().split()]
print(filter_prime(a))