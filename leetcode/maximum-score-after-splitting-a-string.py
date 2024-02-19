class Solution:
    def maxScore(self, s: str) -> int:
        count1 = 0
        count0 = 0
        score = []
        for i in range(len(s)):
            if int(s[i])==1:
                count1+=1
        for i in range(len(s)-1):
            summ=0
            if s[i]=="0":
                count0 +=1
            else:
                count1 -=1
            summ = count0 + count1

            score.append(summ)

        return max(score)
            
        