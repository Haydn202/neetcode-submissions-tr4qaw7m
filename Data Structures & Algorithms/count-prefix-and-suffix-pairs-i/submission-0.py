class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPreix(str1, str2) -> bool:
            return str2.startswith(str1)

        def isSuffix(str1, str2) -> bool:
            return str2.endswith(str1)
            
        count = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if isPreix(words[i], words[j]) and isSuffix(words[i], words[j]):
                    count += 1

        return count