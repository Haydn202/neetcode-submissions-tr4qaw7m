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
                    valid = False
                    break
                if self.pairs[bracket] == stack[len(stack) - 1]:
                    stack.pop()
                else:
                    valid = False
                    break
            else:
                stack.append(bracket)
            
        return valid and len(stack) == 0