class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        rows = len(board)
        cols = len(board[0])

        def dfs(row, col, index) -> bool:
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

            temp = board[row][col]
            board[row][col] = '#'

            if dfs(row + 1, col, index + 1) or \
                dfs(row - 1, col, index + 1) or \
                dfs(row, col + 1, index + 1) or \
                dfs(row, col - 1, index + 1):
                    return True

            board[row][col] = temp

            return False
        
        for i in range(rows):
            for j in range(cols):
                hasWord = dfs(i, j, 0)
                if hasWord:
                    return True
        
        return False



