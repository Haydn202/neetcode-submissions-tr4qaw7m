class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rowLen, colLen = len(grid), len(grid[0])
        freshCount = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    freshCount += 1
        
        time = 0
        while q and freshCount > 0:
            time += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                nabs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in nabs:
                    if min(dr + r, dc + c) < 0:
                        continue
                    
                    if dr + r == rowLen or dc + c == colLen:
                        continue
                    
                    if grid[dr + r][dc + c] == 0 or grid[dr + r][dc + c] == 2:
                        continue
                    
                    grid[dr + r][dc + c] = 2
                    freshCount -= 1
                    
                    q.append((dr + r, dc + c))
            
            
        if freshCount > 0:
            return -1

        return time