import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minSpeed = 1
        maxSpeed = max(piles)

        speed = maxSpeed

        while minSpeed <= maxSpeed:
            mid = (maxSpeed + minSpeed) // 2

            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(float(pile)/mid)

            if totalTime <= h:
                speed = mid
                maxSpeed = mid - 1
            else:
                minSpeed = mid + 1

        return speed  

