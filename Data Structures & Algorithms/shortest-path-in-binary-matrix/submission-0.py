class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        length = 1
        outR = len(grid)
        outC = len(grid[0])
        q = deque()
        q.append((0,0))
        visited = set()
        visited.add((0,0))

        if grid[0][0] == 1:
            return -1
        
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                if r == row - 1 and c == col - 1:
                    return length

                naighbors = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]

                for dr, dc in naighbors:
                    if min(r + dr, c + dc) < 0:
                        continue
                    
                    if r + dr == outR or c + dc == outC:
                        continue
                    
                    if grid[r + dr][c + dc] == 1:
                        continue
                    
                    if (r + dr, c + dc) in visited:
                        continue

                    q.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))
                
            length += 1
            
        return -1



                    


        


