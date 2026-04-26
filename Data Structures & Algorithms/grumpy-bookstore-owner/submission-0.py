class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        time = 0
        maxCustomers = 0
        maxPeriod = 0
        result = 0

        for i in range(len(customers) - minutes + 1):
            customersWhileGrumpy = 0
            for j in range(minutes):
                if grumpy[i + j] == 1:
                    customersWhileGrumpy += customers[i + j]
            if customersWhileGrumpy > maxCustomers:
                maxCustomers = customersWhileGrumpy
                maxPeriod = i
        
        for i in range(minutes):
            grumpy[i + maxPeriod] = 0

        for i in range(len(customers)):
            if grumpy[i] == 0:
                result += customers[i]

        return result