# def removw_duplicates(nums):
#     nums.sort()
#     i = 0
#     while i < len(nums) - 1:
#         if nums[i] == nums[i+1]:
#             nums.remove(nums[i])
#         else:
#             i += 1
#     k = len(nums)
#     return k, nums

#print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))
# very bad runtime 

def remove_duplicate(nums):
    dp = {}
    for i in range(len(nums)):
        if nums[i] in dp:
            dp[nums[i]] += 1
        else:
            dp[nums[i]] = 1
    return len(dp)
print(remove_duplicate([0,0,1,1,1,2,2,3,3,4]))