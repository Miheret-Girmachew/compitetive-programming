class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pre = [0]*(len(s)+1)

        for shift in shifts:
            if shift[2]:
                shift[2] = 1
            else:
                shift[2] = -1
            pre[shift[0]] += shift[2]
            pre[shift[1]+1] -= shift[2]
            
        print(pre)
        
        final = []
        for i in range(len(s)):
            if i != 0: 
                pre[i] += pre[i - 1]
            ss = (ord(s[i]) - ord("a") + pre[i]) % 26 + ord("a")
            final.append(chr(ss))
        print(final)
        return "".join(final)