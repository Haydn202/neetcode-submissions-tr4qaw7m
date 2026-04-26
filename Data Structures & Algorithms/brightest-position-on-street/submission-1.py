class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        points = defaultdict(int)

        for position, ran in lights:
            start = position - ran
            end = position + ran

            points[start] += 1
            points[end + 1] -= 1
        
        current = 0
        maxLight = 0

        result = 0

        for key in sorted(points):
            current += points[key]
            if current > maxLight:
                maxLight = current
                result = key
        
        return result
