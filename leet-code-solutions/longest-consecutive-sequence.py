class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxx=0
        numm = set(nums)
        visited= {}
        for num in numm:
            if num in visited:
                continue
            visited[num]=1
            i=1
            while(num+i in numm):
                if num+i in visited:
                    visited[num]= i + visited[num+i]
                    break
                else:
                    visited[num+i]=-1
                    i+=1
            else:
                visited[num]=i
            maxx= max(maxx, visited[num])
        return maxx
        """class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:  return 0
        uset = set(nums)
        maxi = 1
        for i in uset:
            if i-1 in uset:
                continue
            else:
                conseq = 1
                while i + conseq in uset:
                    conseq += 1
                maxi = max(maxi, conseq)
        return maxi"""