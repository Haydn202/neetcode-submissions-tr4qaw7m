class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        outR = len(grid)
        outC = len(grid[0])

        def landAHo(r, c):
            if r == outR or c == outC:
                return

            if grid[r][c] == "0":
                return
            
            if min(r, c) < 0:
                return
            
            grid[r][c] = "0"

            landAHo(r+1,c)
            landAHo(r-1,c)
            landAHo(r,c+1)
            landAHo(r,c-1)

            return

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    islands = islands + 1
                    landAHo(i, j)
        
        return islands
