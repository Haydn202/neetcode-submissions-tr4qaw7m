class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            rowSet = set()
            for i in range(9):
                if row[i] == ".":
                    continue
                elif row[i] in rowSet:
                    return False
                else:
                    rowSet.add(row[i])
        
        for col in range(9):
            colSet = set()
            for row in range(9):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in colSet:
                    return False
                else:
                    colSet.add(board[row][col])
        
        boxes = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".": continue
                
                box_idx = (r // 3, c // 3)
                if val in boxes[box_idx]:
                    return False
                boxes[box_idx].add(val)
        

        
        return True