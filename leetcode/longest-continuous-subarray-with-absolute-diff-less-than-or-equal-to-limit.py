class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_queue = deque()
        min_queue = deque()
        left = 0
        size = 0
        
        for right, num in enumerate(nums):
            while max_queue and num > max_queue[-1]:
                max_queue.pop()
            while min_queue and num < min_queue[-1]:
                min_queue.pop()
            max_queue.append(num)
            min_queue.append(num)
            
            if max_queue[0] - min_queue[0] > limit:
                if max_queue[0] == nums[left]:
                    max_queue.popleft()
                if min_queue[0] == nums[left]:
                    min_queue.popleft()
                left += 1
                
            size = max(size, right - left + 1)
            
        return size
