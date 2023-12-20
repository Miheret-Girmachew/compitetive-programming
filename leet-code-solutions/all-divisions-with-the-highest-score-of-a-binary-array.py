class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        left_sum = 0
        right_sum = sum(nums)
        maximum = right_sum
        hashh=collections.defaultdict(list)
        hashh[right_sum].append(0)



        for i, num in enumerate(nums):
            left_sum += int(num == 0)
            right_sum -= int(num == 1)
            hashh[left_sum + right_sum].append(i + 1)
            maximum= max(maximum, left_sum + right_sum)
        return hashh[maximum]
                
        
 


    