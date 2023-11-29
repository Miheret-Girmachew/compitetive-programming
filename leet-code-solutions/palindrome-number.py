class Solution:
    def isPalindrome(self, x: int) -> bool:
        b=str(x)
        if b== b[::-1]:
            return True
        else:
            return False
        