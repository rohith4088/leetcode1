from array import *
arr = array('i',[1,2,3,4])
print(arr)
# b Represents signed integer of size 1 byte
# B Represents unsigned integer of size 1 byte
# c Represents character of size 1 byte
# i Represents signed integer of size 2 bytes
# I Represents unsigned integer of size 2 bytes
# f Represents floating-point of size 4 bytes
# d Represents floating-point of size 8 bytes

#accessing the elemnets of an array

arr[3] = 9
arr[2] = 10
print(arr)

arr.insert(3,90)
print(arr)
arr.remove(1)
print(arr)
arr.count(3)
print(arr)
arr.pop(2)
print(arr)
print("--------------------------------")
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Example 1:
# Input: nums = [1,3,2,1]
# Output: true

#brute force solution
def duplicates(nums)-> bool:
    # for i in range(len(nums)):
    #     if nums.count(nums[i])>1:
    #        return True
    # else:
    #     return False
    map = {}
    if len(nums) < 2:
        return False
    for i in range(len(nums)):
        if nums[i] in map:
            return True
        else:
            map[nums[i]] = True
    return True
print(duplicates([1,3,2,1]))

print("--------------------------------")

#Given an array, return the first recurring character
#Example1 : array = [2,1,4,2,6,5,1,4]
#It should return 2
#Example 2 : array = [2,6,4,6,1,3,8,1,2]
#It should return 6

def return_recurring(nums) -> int:
    map = {}
    if len(nums) < 2:
        return 0
    for i in range(len(nums)):
        if nums[i] in map:
            return nums[i]
        else:
            map[nums[i]] = True
            print(map)
    
            
print(return_recurring([2,6,4,6,1,3,8,1,2]))

print("----------------------------------------------------------------")

#internal implementaion for arrays

class my_array():
    def __init__(self):
        self.length = 0
        self.data = {}
    #The attributes of the array class are stored in a dictionary by default.
    #When the __dict__ method is called on an instance of the class it returns the attributes of the class along with their values in a dictionary format
    #Now, when the instance of the class is printed, it returns a class object with its location in memory.
    #But we know when we print the array we get the elements of the array as output
    #When we print the instance of the class, the built-in __str__ method is called. So we can modify the __str__ method inside the class
    #To suit our needs.
    def __str__(self):
        print(self.data.values())
        return str(self.__dict__)
    def get(self,index):
        return self.data[index]
    def push(self,item):
        self.length += 1
        self.data[self.length - 1] = item
    def pop(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item
    def insert(self,index,item):
        self.length += 1
        for i in range(self.length - 1,index,-1):
            self.data[i] = self.data[i-1]
        self.data[index] = item
    def delete(self,index):
        for i in range(index,self.length -1):
            self.data[i] = self.data[i+1]
        del self.data[self.length - 1]
        self.length -= 1
        
        
        
        
arr = my_array()
print(arr)
print("-"*100)
arr.push(6)
#{'length': 1, 'data': {0: 6}}

arr.push(2)
#{'length': 2, 'data': {0: 6, 1: 2}}

arr.push(9)
#{'length': 3, 'data': {0: 6, 1: 2, 2: 9}}

arr.pop()
#{'length': 2, 'data': {0: 6, 1: 2}}

arr.push(45)
arr.push(12)
arr.push(67)
#{'length': 5, 'data': {0: 6, 1: 2, 2: 45, 3: 12, 4: 67}}

arr.insert(3,10)
#{'length': 6, 'data': {0: 6, 1: 2, 2: 45, 3: 10, 4: 12, 5: 67}}

arr.delete(4)
#{'length': 5, 'data': {0: 6, 1: 2, 2: 45, 3: 10, 4: 67}}

print(arr.get(1))
#2

print(arr)
#The outputs given after each function call are the outputs obtained by calling print(arr) and not by the function calls themselves

print("----------------------------------------------------------------")    
# #Find the largest word in a given string
# #Examples
# #Input: "fun&!! time"
# #Output: time


def largest_word(s):
    s = s.split()
    
    length= {}
    for i in range(len(s)):
        if s[i].isalpha():
            length[s[i]] = len(s[i])
    max_length = max(length.values())
    for word, length in length.items():
        if length == max_length:
            print(word)
largest_word("rohith is a good boy!!!!!")



# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.
# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


def longest_subsequence(nums) -> list:
    sets = list(set(nums))
    sets.sort()
    sequence = []
    for i in range(len(sets)):
        if sets[i] + 1 in sets:
            sequence.append(sets[i])
        else:
            sequence.append(sets[i])  # Append the last element of the consecutive sequence
            break
    return list(len(sequence))

print(longest_subsequence([100,4,200,1,3,2])) #only passes 31/75 test cases


