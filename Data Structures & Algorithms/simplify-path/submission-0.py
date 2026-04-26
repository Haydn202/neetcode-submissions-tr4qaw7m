class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path:
            return

        stack = []
        result = ""

        split = path.split('/')

        for item in split:
            if len(item) < 1:
                continue

            if item == ".":
                continue
            
            if item == "..":
                if len(stack) > 0:
                    stack.pop()
                continue
            
            stack.append(item)
        
        result = '/' + '/'.join(stack)

        return result