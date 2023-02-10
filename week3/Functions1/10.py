def r(nums):
    a = []
    for i in range(0, len(nums)):
        try:
            b = a.index(nums[i])
        except ValueError:
            a.append(nums[i])
    return a


nums = [int(k) for k in input().split()]
print(r(nums))
