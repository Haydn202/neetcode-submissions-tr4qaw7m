class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0, 0, 0]

        for num in nums:
            buckets[num] += 1
        
        index = 0

        for i in range(len(buckets)):
            count = buckets[i]
            for j in range(count):
                nums[index] = i
                index += 1
                
