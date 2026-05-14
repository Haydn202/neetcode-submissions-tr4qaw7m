class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []

        left = 0
        right = len(numbers) - 1

        while left < right:
            numSum = numbers[left] + numbers[right]

            if numSum == target:
                return [left + 1, right + 1]
            
            if numSum > target:
                right -= 1

            if numSum < target:
                left += 1

        return result