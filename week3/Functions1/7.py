def has_33(nums):
    for i in range (1, len(nums)):
        if nums[i] == 3 and nums[i - 1] == 3:
            return True
    return False

nums = [int(k) for k in input().split()]
print(has_33(nums))