class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        case1 = nums[:-1]
        case2 = nums[1:]
        
        memo = {}

        def recurse(i, items):
            if i in memo:
                return memo[i]
            
            if i > len(items) - 1:
                return 0

            money = items[i]

            rob = recurse(i + 2, items) + money
            dontRob = recurse(i + 1, items)

            memo[i] = max(rob, dontRob)

            return memo[i]
        
        result1 = recurse(0, case1)
        memo.clear()
        result2 = recurse(0, case2)
        return max(result1, result2)