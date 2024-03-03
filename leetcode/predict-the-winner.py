class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def recursion(i, j, turn):
            if i == j:
                if turn:
                    return [nums[i], 0]
                else:
                    return [0, nums[i]]
            left = recursion(i+1, j, not turn)
            right = recursion(i, j-1, not turn)
            if turn:
                if left[0] + nums[i] - left[1] > right[0] + nums[j] - right[1]:
                    left[0] += nums[i]
                    return left
                else:
                    right[0] += nums[j]
                    return right
            else:
                if left[1] + nums[i] - left[0] > right[1] + nums[j] - right[0]:
                    left[1] += nums[i]
                    return left
                else:
                    right[1] += nums[j]
                    return right
        
        result = recursion(0, len(nums) - 1, True)
        return result[0] >= result[1]
        