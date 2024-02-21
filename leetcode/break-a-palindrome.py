class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        found = False
        listt = []
        for s in palindrome:
            listt.append(s)
        for i in range(len(listt)):
            if listt[i] != "a":
                temp = listt[i]
                listt[i] = "a"
                if listt != listt[::-1]:
                    found = True
                    listt[i] = "a"
                    break
                else:
                    listt[i] = temp
        if found == False:
            listt[-1] = "b"
        return "".join(listt)
        