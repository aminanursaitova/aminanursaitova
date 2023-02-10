def solve(numheads, numlegs):
    for i in range (1, numheads):
        if i * 2 + (numheads - i) * 4 == numlegs:
            print("There are", i, "chikens and", numheads - i, "rabbits in the farm.")

a = int(input())
b = int(input())
solve(a, b)