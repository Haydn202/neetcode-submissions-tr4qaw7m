class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def getHash(string: str):
            h = {}

            for char in string:
                if char in h:
                    h[char] += 1
                else:
                    h[char] = 1
            
            return h
        
        s1Hash = getHash(s)
        s2Hash = getHash(t)

        return s1Hash == s2Hash