class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count=0
        maxx=0
        hashh={}
        l=0
        for r in range(len(fruits)):
            hashh[fruits[r]]=hashh.get(fruits[r],0)+1
            while(len(hashh)>2):
                hashh[fruits[l]]-=1
                if hashh[fruits[l]]==0:
                    del hashh[fruits[l]]
                l+=1
            count=r-l+1
            maxx=max(maxx,count)
        return maxx



        