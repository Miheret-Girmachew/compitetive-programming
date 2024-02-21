class Solution:
    def longestPalindrome(self, s: str) -> int:
        summ = 0
        ones = 0
        count = Counter(s)
        for val in count:
            if count[val] % 2 == 0:
                summ += count[val]
            else:
                if count[val] > 1:
                    summ += int(count[val]/2)*2
                    count[val] -= int(count[val]/2)*2
                
        for val in count:
            if count[val]== 1:
                summ += 1
                break
                
        return summ
        
        