class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        ans = []
        
        for word in words:
            if word[0].lower() in row1:
                l = 0
                while l < len(word)and word[l].lower() in row1:
                    l += 1
                if l== len(word):
                    ans.append(word)
            elif word[0].lower() in row2:
                l = 0
                while l < len(word) and word[l].lower() in row2:
                    l += 1
            
                if l== len(word):
                    ans.append(word)
            elif word[0].lower() in row3:
                l = 0
                while l < len(word) and word[l].lower() in row3:
                    l += 1
                if l==len(word):
                    ans.append(word)
                
                
        return ans

                    