import random
global x
x = random.randrange(1, 20)
k = 0
def game(name, k):
    print("Take a guess.")
    a = int(input())
    print()
    if a == x:
        if k == 1:
            print("Good job, ", name, "! You guessed my number in ", k, " guess!", sep="")
        else:
            print("Good job, ", name, "! You guessed my number in ", k, " guesses!", sep="")
        return
    elif a < x:
        print("Your guess is too low.")
        k += 1
        game(name, k)
    else:
        print("Your guess is too big.")
        k += 1
        game(name, k)

print("Hello! What is your name?")
name = input()
print()
print("Well, ", name," , I am thinking of a number between 1 and 20.", sep="")
game(name, k)