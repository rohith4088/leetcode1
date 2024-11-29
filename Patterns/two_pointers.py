#target sum

def two_pointers_for_target_sum(nums : list,target):
    l , r = 0 , len(nums) - 1 
    while l < r:
        current_sum = nums[l] + nums[r]
        if current_sum == target:
            return [nums[l] + nums[r]]
        elif current_sum < target:
            l += 1
        else:
            r -= 1
    return None
        

         