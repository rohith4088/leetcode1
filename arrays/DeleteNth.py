#naive way of doing this
#define a fucntion with two inputs list and a n(the corresponds to the allowed repetiotion)
#define a result list
#traverse through the list and check if the occurence of each element is less than "n"
#if this condition is true then append to the result list
#return result

def Delete_naive(nums : list[int] ,  n :int) -> list[int]:
    res = []
    for num in nums:
        if nums.count(nums[num]) < n:
            res.append(num)
    return res


nums = [1,2,1,2,1,2,3,4]
n = 2
print(*Delete_naive(nums , n) , sep = ',')

import collections
from memory_profiler import profile
file = open("Deletenth.log" , 'w+')

@profile(stream = file)
def Deelete(nums : list[int] , n : int) -> list[int]:
    res = []
    map = collections.defaultdict(int)
    for num in nums:
        if map[num] < n:
            res.append(num)
            map[num] += 1
    return res

nums2 = [1,2,1,2,1,2,3,4,5]
n = 2
print(*Deelete(nums2 , n), sep = ',')

