# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        pairsList = []
        
        for i in range(len(pairs)):
            pointer = i - 1

            while pointer >= 0 and pairs[pointer + 1].key < pairs[pointer].key:
                temp = pairs[pointer + 1]
                pairs[pointer + 1] = pairs[pointer]
                pairs[pointer] = temp
                pointer -= 1
            
            pairsList.append(pairs[:])
        
        return pairsList



