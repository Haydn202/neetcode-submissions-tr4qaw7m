class Solution:
    pairs = {
        ']': '[',
        ')': '(',
        '}': '{',
    }

    def isValid(self, s: str) -> bool:
        stack = []
        count = 0
        valid = True

        for bracket in s:
            if bracket in self.pairs:
                if count > 0 and self.pairs[bracket] == stack[count - 1]:
                    stack.pop()
                    count -= 1
                else:
                    valid = False
                    break
            else:
                stack.append(bracket)
                count += 1
            
        return valid and count == 0