class bank_acc:
    def __init__(a, o, b):
        a.owner = o
        a.balance = b

    def inp(a):
        a.owner = input()
        a.balance = int(input())

    def deposit(a, x):
        a.balance += x
        print(x, " money has been deposited. Your current balance is ", a.balance, ". Thank You for using our bank, ", a.owner, "<3")#, sep = "")

    def withdraw(a, x):
        if x < a.balance:
            a.balance -= x
            print(x, " money has been withdrawn. Your current balance is ", a.balance, ". Thank You for using our bank, ", a.owner, "<3")#, sep = "")
        else:
            print("Withdrawal error, try smaller amount. Your current balance is ", a.balance, ". Thank You for using our bank, ", a.owner, "<3")#, sep = "")

    def bank_sys(a, request):
        if request == "deposit":
            print("How much money do you want to deposit?")
            b = int(input())
            a.deposit(b)

u1 = bank_acc("MyMelody", 15)
u2 = bank_acc(0, 0)
u2.inp()
u1.deposit(13)
u1.withdraw(5)
u1.withdraw(50)
u2.deposit(16)
u2.withdraw(3)
u2.withdraw(70)