class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = []
        count = 0
        for i in range(len(strs[0])):
            val = []
            for word in strs:
                val.append(word[i])
            ans.append(val)
      

        for listt in ans:
            if listt==sorted(listt):
                continue
            else:
                count+=1

        return count
        


        