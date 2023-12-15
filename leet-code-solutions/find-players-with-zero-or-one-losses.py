class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = []
        loser = {}
        ans1 = []
        ans2 = []

        for i in range(len(matches)):
            winner.append(matches[i][0])
            loser[matches[i][1]]=loser.get(matches[i][1], 0)+1

        for num in winner:
            if num not in loser:
                ans1.append(num)
   
        for key, value in loser.items():
            if value==1:
                ans2.append(key)

        sortedans1 = sorted(list(set(ans1)))
        sortedans2 = sorted(list(set(ans2)))
       
        return [sortedans1, sortedans2]

    


        