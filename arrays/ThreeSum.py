#Brute Force Approach
# def threesum(nums):
#     res = []
#     for i in range(len(nums)):   
#         for j in range(i+1 , len(nums)):
#             for k in range(j+1,len(nums)):
#                 if nums[i] + nums[j] + nums[k] == 0:
#                     res.append([nums[i],nums[j],nums[k]])
#     return res

# print(threesum([-1,0,1,2,-1,-4]))

#USING TWO POINTER APPROACH
#not sure how it works

def threesum(nums):
    res = []
    nums.sort()
    for i , a in enumerate(nums):
        if i > 0 and nums[i-1] == a:
            continue
        l , r = i + 1, len(nums) -1 
        while  l < r :
            threesum = a + nums[l] + nums[r]
            if threesum > 0:
                r -= 1
            elif threesum < 0:
                l += 1
            else:
                res.append([a,nums[l],nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1
    return res
print(threesum([-1,0,1,2,-1,-4]))
        
