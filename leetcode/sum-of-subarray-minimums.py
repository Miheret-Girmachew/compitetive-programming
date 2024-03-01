class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # n = len(arr)
        # left = [-1] * n 
        # right = [n] * n
        # stack = []

        # for i, value in enumerate(arr):
        #     while stack and arr[stack[-1]] >= value:  
        #         stack.pop()  
        #     if stack:
        #         left[i] = stack[-1]  
        #     stack.append(i) 

        # stack = [] 

        # for i in range(n - 1, -1, -1):  
        #     while stack and arr[stack[-1]] > arr[i]: 
        #         stack.pop()  
        #     if stack:
        #         right[i] = stack[-1]  
        #     stack.append(i) 

        # mod = 10**9 + 7 

        # result = sum((i - left[i]) * (right[i] - i) * value for i, value in enumerate(arr)) % mod
      
        # return result 
        ans = 0
        stack = []
        for i, val in enumerate(arr):
            while stack and val<stack[-1][1]:
                index, value = stack.pop()
                if stack:
                    left = index-stack[-1][0]
                else:
                    left = index+1
                right = i - index
                ans = (ans+(value*left*right))%(10**9 + 7)
            stack.append((i, val))
        for i in range(len(stack)):
            index, value = stack[i]
            if i > 0:
                left = index - stack[i-1][0]
            else:
                left = index+1
            right = len(arr)-index
            ans= (ans+value*left*right)%(10**9 + 7)
        return ans



        