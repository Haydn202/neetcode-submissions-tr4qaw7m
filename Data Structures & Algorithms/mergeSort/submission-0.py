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

        for i in range(len(left) + len(right)):
            if leftPointer >= len(left):
                merged.append(right[rightPointer])
                rightPointer += 1
            elif rightPointer >= len(right):
                merged.append(left[leftPointer])
                leftPointer += 1
            elif left[leftPointer].key <= right[rightPointer].key:
                merged.append(left[leftPointer])
                leftPointer += 1
            elif right[rightPointer].key < left[leftPointer].key:
                merged.append(right[rightPointer])
                rightPointer += 1
        
        return merged
