class Solution:
    pairs = {
        ']': '[',
        ')': '(',
        '}': '{',
    }

    def isValid(self, s: str) -> bool:
        stack = []
        valid = True

        for bracket in s:
            if bracket in self.pairs:
                if len(stack) == 0:
                    return False
                if self.pairs[bracket] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
            
        return valid and len(stack) == 0