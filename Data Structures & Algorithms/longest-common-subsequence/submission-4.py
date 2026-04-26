class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def solve(p1, p2) -> int:
            if p1 == len(text1) or p2 == len(text2):
                return 0
            
            if (p1, p2) in memo:
                return memo[(p1, p2)]
            
            if text1[p1] == text2[p2]:
                res = 1 + solve(p1 + 1, p2 + 1)
            else:
                res = max(solve(p1 + 1, p2), solve(p1, p2 + 1))

            memo[(p1, p2)] = res
            return res

        return solve(0, 0)



            