def canJump(nums):

    n = 0
    if n >= len(nums)-1:
        return True
    while n < len(nums):
        if n+nums[n] >= len(nums) -1:
            return True
        if nums[n] == 0:
            return False

        possible_jumps = nums[n+1:n+nums[n]+1]
        n = n + 1
        last = nums[n] - len(possible_jumps)
        changes = 0
        for i in range(1, len(possible_jumps)):
            if possible_jumps[i]-(len(possible_jumps)-i) >= last:
                last = possible_jumps[i]-(len(possible_jumps)-i)
                changes = i
        n += changes

    else:
        return True
print(canJump([4,4,4,0,3,1,2,1,1,3,4]))