class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        i = 0

        for num in nums:
            dif = target - num
            if dif in seen:
                return [seen[dif], i]
            seen[num] = i
            i += 1
        
        return [0, 0]

