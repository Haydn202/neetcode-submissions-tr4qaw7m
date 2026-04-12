import math

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dist = math.sqrt(x**2 + y**2)
    
    def __lt__(self, other):
        return self.dist > other.dist

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pointHeap = []

        for point in points:
            heapq.heappush(pointHeap, Point(point[0], point[1]))
            if len(pointHeap) > k:
                heapq.heappop(pointHeap)
        
        return [[p.x, p.y] for p in pointHeap]