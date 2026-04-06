class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        left = nums1[:m]
        right = nums2

        leftPointer = 0
        rightPointer = 0

        for i in range(len(nums1)):
            if leftPointer >= m:
                nums1[i] = right[rightPointer] 
                rightPointer += 1
            elif rightPointer >= n:
                nums1[i] = left[leftPointer]
                leftPointer += 1
            elif left[leftPointer] <= right[rightPointer]:
               nums1[i] = left[leftPointer]
               leftPointer += 1
            else:
               nums1[i] = right[rightPointer] 
               rightPointer += 1
        

