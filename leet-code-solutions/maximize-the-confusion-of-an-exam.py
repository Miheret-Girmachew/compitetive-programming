class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        maxx=0
        l=0
        ans={'T':0, 'F':0}

        for r in range(len(answerKey)):
            while min(ans['T'], ans['F'])>k:
                ans[answerKey[l]]-=1
                l+=1
            ans[answerKey[r]]+=1
            if min(ans['T'], ans['F'])<=k:
                maxx=max(maxx, r-l+1)
            
        return maxx