class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]
        if start_color == color:
            return image
            
        intialColour = image[sr][sc]
        maxR = len(image)
        maxC = len(image[0])


        def fill(colour: int, r: int, c: int):
            if intialColour == color: 
                return

            if min(r, c) < 0:
                return
            
            if r == maxR or c == maxC:
                return

            if image[r][c] != intialColour:
                return
            
            image[r][c] = colour

            fill(colour, r + 1, c)
            fill(colour, r , c + 1)
            fill(colour, r - 1, c)
            fill(colour, r, c - 1)

            return
        
        fill(color, sr, sc)
        return image

            
