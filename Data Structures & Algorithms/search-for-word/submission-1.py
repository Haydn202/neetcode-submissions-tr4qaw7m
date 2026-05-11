class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        rows = len(board)
        cols = len(board[0])

        def dfs(row, col, word, index) -> bool:
            if index == len(word):
                return True
            
            if row < 0 or col < 0:
                return False
            
            if row >= rows or col >= cols:
                return False
            
            if (row, col) in visited:
                return False

            if word[index] != board[row][col]:
                return False

            visited.add((row, col))

            down = dfs(row + 1, col, word, index + 1)
            right = dfs(row, col + 1, word, index + 1)
            up = dfs(row - 1, col, word, index + 1)
            left = dfs(row, col - 1, word, index + 1)

            visited.remove((row, col))

            return down or right or up or left
        
        for i in range(rows):
            for j in range(cols):
                hasWord = dfs(i, j, word, 0)
                if hasWord:
                    return True
        
        return False



