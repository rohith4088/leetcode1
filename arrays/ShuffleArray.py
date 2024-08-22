import random

class Solution():
    def __init__(self , nums : list[int] , *args):
        self.nums = nums
        self.original_nums = nums.copy()
    def reset(self)->list[int]:
        return self.original_nums
    def shuffle(self)->list[int]:
        #Shuffling logic Fisher-Yates shuffle
        for i in range(len(self.nums) - 1, 0, -1):
            j = random.randint(0, i)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums

nums = [1, 2, 3]
solution = Solution(nums)
print("Original:", nums)
shuffled = solution.shuffle()
print("Shuffled:", shuffled)
reset = solution.reset()
print("Reset:", reset)
shuffled_again = solution.shuffle()
print("Shuffled again:", shuffled_again)
