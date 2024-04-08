def threesum(nums):
    res = []
    for i in range(len(nums)):   
        for j in range(i+1 , len(nums)):
            for k in range(j+1,len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i],nums[j],nums[k]])
    return res

print(threesum([-1,0,1,2,-1,-4]))
