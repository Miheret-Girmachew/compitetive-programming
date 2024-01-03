class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count=0
        summ=0
        for i in range(len(costs)):
            summ+=costs[i]
            if summ<=coins:
                count+=1
            else:
                break
        return count


        