class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        memo = {}
        
        def recurse(i):
            if i in memo:
                return memo[i]

            if i > len(nums) - 1:
                return 0
            
            money = nums[i]

            rob = recurse(i + 2) + money
            dontRob = recurse(i + 1)

            memo[i] = max(rob, dontRob)

            return memo[i]
        
        return recurse(0)
