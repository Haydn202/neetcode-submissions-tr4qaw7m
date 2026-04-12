import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stoneHeap = stones
        heapq.heapify_max(stoneHeap)

        while len(stoneHeap) > 1:
            x = heapq.heappop_max(stoneHeap)
            y = heapq.heappop_max(stoneHeap)

            if x == y:
                continue

            if x > y:
                x = x - y
                heapq.heappush_max(stoneHeap, x)
        
        if len(stoneHeap) < 1:
            return 0

        return heapq.heappop_max(stoneHeap)

