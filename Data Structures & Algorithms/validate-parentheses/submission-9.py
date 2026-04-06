class Solution:
    pairs = {
        ']': '[',
        ')': '(',
        '}': '{',
    }

    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket in self.pairs:
                if not stack:
                    return False
                if self.pairs[bracket] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
            
        return len(stack) == 0