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
        width, height = len(boxGrid), len(boxGrid[0])

        rotated = [[""] * width for _ in range(height)]

        for r in range(width):
            for c in range(height):
                rotated[c][width - 1 - r] = boxGrid[r][c]

        return rotated
