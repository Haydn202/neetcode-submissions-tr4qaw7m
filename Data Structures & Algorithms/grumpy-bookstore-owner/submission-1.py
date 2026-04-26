class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        left = 0
        maxWindow, window = 0, 0
        satisfied = 0

        for r in range(len(customers)):
            if grumpy[r]:
                window += customers[r]
            else:
                satisfied += customers[r]
            
            if r - left + 1 > minutes:
                if grumpy[left]:
                    window -= customers[left]
                left += 1
            maxWindow = max(window, maxWindow)


        return satisfied + maxWindow