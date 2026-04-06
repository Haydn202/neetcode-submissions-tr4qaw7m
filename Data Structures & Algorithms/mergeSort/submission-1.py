# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        
        mid = len(pairs) // 2
        left = self.mergeSort(pairs[:mid])
        right = self.mergeSort(pairs[mid:])
        
        return self.merge(left, right)
        
    def merge(self, left: List[Pair], right: List[Pair]) -> List[Pair]:
        merged = []

        leftPointer = 0
        rightPointer = 0

        while leftPointer < len(left) and rightPointer < len(right):
            if left[leftPointer].key <= right[rightPointer].key:
                merged.append(left[leftPointer])
                leftPointer += 1
            else:
                merged.append(right[rightPointer])
                rightPointer += 1

        merged.extend(left[leftPointer:])
        merged.extend(right[rightPointer:])
        
        return merged
