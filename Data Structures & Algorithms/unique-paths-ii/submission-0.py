class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}

        def getPaths(r, c) -> int:

            if r == len(obstacleGrid) or c == len(obstacleGrid[0]):
                return 0

            if obstacleGrid[r][c] == 1:
                return 0

            if (r, c) in memo:
                return memo[(r, c)]

            if r == len(obstacleGrid) - 1 and c == len(obstacleGrid[0]) - 1:
                return 1

            memo[(r, c)] = getPaths(r + 1, c) + getPaths(r, c + 1)

            return memo[(r, c)] 

        return getPaths(0, 0) 