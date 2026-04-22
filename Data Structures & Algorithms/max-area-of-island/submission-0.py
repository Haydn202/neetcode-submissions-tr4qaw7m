class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        outR = len(grid)
        outC = len(grid[0])

        maxIslandSize = 0

        def landAHo(r, c) -> int:
            if min(r, c) < 0:
                return 0

            if r == outR or c == outC:
                return 0

            if grid[r][c] == 0:
                return 0

            grid[r][c] = 0

            size = 1

            size += landAHo(r + 1, c)
            size += landAHo(r - 1, c)
            size += landAHo(r, c + 1)
            size += landAHo(r, c - 1)

            return size
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    size = landAHo(i, j)
                    if size > maxIslandSize:
                        maxIslandSize = size
        
        return maxIslandSize

            
