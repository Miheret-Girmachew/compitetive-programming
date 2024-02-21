class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counterT = Counter(t)
        counterS = defaultdict(int)
        left = 0
        right = 0
        min_len = float('inf')
        min_window = ""
        
        while right < len(s):
            if s[right] in counterT:
                counterS[s[right]] += 1
            
            while all(counterS[char] >= counterT[char] for char in counterT) and left <= right:
                current_len = right - left + 1
                if current_len < min_len:
                    min_len = current_len
                    min_window = s[left:right+1]
                
                counterS[s[left]] -= 1
                left += 1
            
            right += 1
        
        return min_window