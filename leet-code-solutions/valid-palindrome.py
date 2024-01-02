class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=''
        for letter in s.lower():
            if letter.isalnum():
                s1+=letter
        return  s1==s1[::-1]
      
      
        