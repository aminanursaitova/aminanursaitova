def histogram(nums):
    for a in nums:
        for i in range(a):
            print("*", end="")
        print()
    return

nums = [int(k) for k in input().split()]
histogram(nums)
