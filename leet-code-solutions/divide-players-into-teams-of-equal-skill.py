class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        right= len(skill)-1
        left=0
        k=skill[right]+skill[left]
        summ=0
       

        while left< right:
            while skill[right]+skill[left]!=k:
                return -1
            mult=1
            mult=skill[right]*skill[left]
            summ+=mult
            left+=1
            right-=1
        return summ


        