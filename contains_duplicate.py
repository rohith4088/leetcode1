#Given an array of integers, find if the array contains any duplicates.
#Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
#Example 1:
#Input: [1,2,3,1]
#Output: true
#Example 2:
#Input: [1,2,3,4]
#Output: false
# naive approch
def brute_force(array):
    for i in range(len(array)-1):
        for j in range (i+1,len(array)):
            if array[i] == array[j]:
                return True
    return False
array = [1,2,3,1,23,1,2,3]
print(brute_force(array))
#An even better solution can be using a dictionary.
#As we loop through the array, we'll check first if the current element is present in the dictionary
#If yes, we return True
#If no, we add the element to the dictionary.
#Since looking up in a dictionary is O(1) time, overall complexity would be O(n)
def efficeint(array):
    map = {}
    if len(array) < 2:
        return False
    for i in range (len(array)):
        if array[i] in map:
            return True
        else:
            map[array[i]] = True
    return False
            
            
print(efficeint([1,2,3,4,4]))
