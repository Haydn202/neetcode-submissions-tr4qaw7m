class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def climb(i):
            if i <= 2:
                return i

            if i in cache:
                return cache[i]

            cache[i] = climb(i -1) + climb(i - 2)

            return cache[i]

        return climb(n)