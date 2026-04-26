class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        
        def getPaths(r: int, c: int) -> int:
            if r == m or c == n:
                return 0
            
            if (r, c) in memo:
                return memo[(r, c)]
            
            if r == m - 1 and c == n - 1:
                return 1
            
            memo[(r, c)] = getPaths(r + 1, c) + getPaths(r, c + 1)
            
            return memo[(r, c)]
        
        return getPaths(0, 0)