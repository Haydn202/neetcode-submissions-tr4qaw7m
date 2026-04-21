class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        intialColour = image[sr][sc]
        maxR = len(image)
        maxC = len(image[0])

        visited = set()

        def fill(colour: int, r: int, c: int):
            if (r,c) in visited:
                return
                
            if min(r, c) < 0:
                return
            
            if r == maxR or c == maxC:
                return

            if image[r][c] is not intialColour:
                return

            visited.add((r,c))
            
            image[r][c] = colour

            fill(colour, r + 1, c)
            fill(colour, r , c + 1)
            fill(colour, r - 1, c)
            fill(colour, r, c - 1)

            return
        
        fill(color, sr, sc)
        return image

            
