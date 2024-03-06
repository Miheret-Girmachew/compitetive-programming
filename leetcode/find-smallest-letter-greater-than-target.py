class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        r = len(letters)-1
        while l <= r:
            mid = (l+r)//2
            if letters[mid] > target:
                r = mid -1
            else:
                l = mid + 1
        if l==len(letters):
            return letters[0]
        return letters[l]
        
        