class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if self.inRange(row, target):
                return self.contains(row, target)
        
        return False
    
    def inRange(self, row: List[int], target) -> bool:
        if target >= row[0] and target <= row[-1]:
            return True
        return False

    def contains(self, row, target) -> bool:
        left = 0
        right = len(row) - 1

        while left <= right:
            mid = (left + right) // 2

            if row[mid] > target:
                right = mid - 1
            elif row[mid] < target:
                left = mid + 1
            else:
                return True
        
        return False