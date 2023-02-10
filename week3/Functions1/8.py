def spy_game(nums):
    k = 0
    spy = [0, 0, 7]
    for i in range (1, len(nums)):
        if nums[i] == spy[k]:
            k += 1
        if k == 3:
            return True
    return False

nums = [int(k) for k in input().split()]
print(spy_game(nums))