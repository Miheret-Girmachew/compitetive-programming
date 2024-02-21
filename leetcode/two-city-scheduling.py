class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        cost = []
        for c in costs:
            cost.append(c[1]-c[0])
        hs = {}
        for c in costs:
            hs[c[1]-c[0]] = [c[0], c[1]]
        cost.sort()
        summ = 0
        print(cost)
        print(hs)
        # print(hs[cost[0]][1])
        for i in range(len(cost)):
            if i < len(cost)//2:
                summ += hs[cost[i]][1]
            else:
                summ += hs[cost[i]][0]
        return summ
        """
        costs.sort(key = lambda x: abs(x[0]-x[1]), reverse =True)
        B=A=len(costs)/2
        print(costs)
        tot = 0
        for ac, bc in costs:
            if B==0 or (A>0 and ac <= bc):
                tot += ac
                A-=1
            else:
                tot += bc
                B-=1
        return tot






