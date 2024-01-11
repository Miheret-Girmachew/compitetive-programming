class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        countt = blocks[:k].count("W")
        minn = countt
        l = 0
        for r in range(k,len(blocks)):
            if blocks[r]=="W":
                countt+=1
            if blocks[l]=="W":
                countt-=1
                l+=1
            else:
                l+=1
    
            minn = min(countt, minn)
        return minn


        