class solution:
    def rob (self,nums):
        if not  nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [None] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(nums[i] + dp[i-2],dp[i-1])
            
        return dp[-1]
        
if __name__ == "__main__":
    s = solution()
    print(s.rob([2,7,9,3,1]))