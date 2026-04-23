class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        increasing = True
        decreasing = True

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                decreasing = False
            if nums[i] > nums[i + 1]:
                increasing = False
        
        if increasing or decreasing:
            return True
        
        return False

