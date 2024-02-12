# from array import *
# arr = array('i',[1,2,3,4])
# print(arr)
# b Represents signed integer of size 1 byte
# B Represents unsigned integer of size 1 byte
# c Represents character of size 1 byte
# i Represents signed integer of size 2 bytes
# I Represents unsigned integer of size 2 bytes
# f Represents floating-point of size 4 bytes
# d Represents floating-point of size 8 bytes

#accessing the elemnets of an array

# arr[3] = 9
# arr[2] = 10
# print(arr)

# arr.insert(3,90)
# print(arr)
# arr.remove(1)
# print(arr)
# arr.count(3)
# print(arr)
# arr.pop(2)
# print(arr)

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Example 1:
# Input: nums = [1,3,2,1]
# Output: true

#brute force solution
# def duplicates(nums)-> bool:
#     # for i in range(len(nums)):
#     #     if nums.count(nums[i])>1:
#     #        return True
#     # else:
#     #     return False
#     map = {}
#     if len(nums) < 2:
#         return
#     for i in range(len(nums)):
#         if nums[i] in map:
#             return True
#         else:
#             map[nums[i]] = True
           
    
    
# print(duplicates([1,3,2,1]))



#Given an array, return the first recurring character
#Example1 : array = [2,1,4,2,6,5,1,4]
#It should return 2
#Example 2 : array = [2,6,4,6,1,3,8,1,2]
#It should return 6

def return_recurring(nums) -> int:
    map = {}
    if len(nums) < 2:
        return
    for i in range(len(nums)):
        if nums[i] in map:
            return nums[i]
        else:
            map[nums[i]] = True
            print(map)
    
            
print(return_recurring([2,6,4,6,1,3,8,1,2]))