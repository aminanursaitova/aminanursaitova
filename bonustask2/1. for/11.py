N=int(input())
su=0
sum=0
for i in range(N-1):
    a=int(input())
    su+=a
for i in range(1, N+1):
    sum+=i
x=sum-su
print(x)
