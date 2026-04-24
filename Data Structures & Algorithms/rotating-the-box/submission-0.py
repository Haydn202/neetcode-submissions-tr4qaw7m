class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        # drop stones
        for row in boxGrid:
            lowest = len(row) - 1
            for col in range(len(row) - 1, -1, -1):
                if row[col] == "#":
                    row[col], row[lowest] = ".", "#"
                    lowest = lowest - 1
                if row[col] == "*":
                    lowest = col - 1

        #rotate
        height, width = len(boxGrid), len(boxGrid[0])

        rotated = [[""] * height for _ in range(width)]

        for r in range(height):
            for c in range(width):
                rotated[c][height - 1 - r] = boxGrid[r][c]

        return rotated




            

        