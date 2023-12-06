class Solution:
    def printVertically(self, s: str) -> List[str]:
        neww=[]
        values=s.split()
        maximum=0
        for word in values:
            maximum=max(maximum, len(word))
            
    
        for i in range(maximum):
            wordd = ""
            for word in values:
                if i < len(word):
                    wordd += word[i]
                else:
                    wordd += " " 
                
            neww.append(wordd.rstrip()) 
        return neww


        
        