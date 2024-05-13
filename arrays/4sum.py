def FourSum(nums,target):
    nums.sort()
    res,quad = [],[]
    #the fucntion ksum is a recursive function that is generalsied for any number of k
    #the base is that if two sumII
    
    def ksum(k,start,target):
        if k != 2:
            for i in range(start,len(nums) - k +1): #len(nums) - k  + 1 is used to avoid inde out of range , this also abvoid duplicates in theformat for quads
                if nums[i] == nums[i-1] and i > start: # i > start handels the forst time the loop strats from the frst number
                    continue
                quad.append(nums[i])
                ksum(k-1,i+1,target - nums[i])
                quad.pop()
            return
        #base case of 2sum II
        l , r = start , len(nums) - 1
        while l < r:
            if nums[l] + nums[r] > target:
                r -= 1
            elif nums[l] + nums[r] < target:
                l += 1 
            else:
                res.append(quad+[nums[l],nums[r]])
                l += 1 #you can arbitarly choose l or r to increment
                #if you dont increment the loop will run infinitely
                #this is because the loop will keep on adding the same number
                #to the quad list
                while l < r and nums[l] == nums[l-1]:
                    l += 1
    ksum(4,0,target)
    return res
print(FourSum([1, 0, -1, 0, -2, 2],0))