class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1] 
        row_prev = self.getRow(rowIndex-1)
        print(row_prev)
        ans = [1]
        i = 1
        while i<len(row_prev):
            ans.append(row_prev[i-1] + row_prev[i])
            i+=1
        ans.append(1)
        return ans
        
        
        
            
        
        