#i dindt write this
def threesum(nums, target):
    nums.sort()
    closest_sum = float('inf')
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            current_sum = nums[i] + nums[l] + nums[r]
            if current_sum == target:
                return target
            elif current_sum < target:
                l += 1
            else:
                #r -= 1
                #closest_sum = min(current_sum, abs(current_sum - target))
                l += 1
                while nums[l]== nums[l-1] and l < r:
                    l += 1
    return current_sum

print(threesum([-1, 2, 1, -4], 1)) # Output: 2
print(threesum([0, 0, 0], 1)) # Output: 0
