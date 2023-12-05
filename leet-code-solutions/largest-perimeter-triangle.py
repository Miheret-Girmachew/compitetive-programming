class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        summ=0
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            num1= nums[i]
            num2= nums[i+1]
            num3= nums[i+2]
            if num1 < num2 + num3:
                summ= num1+num2+num3
                return summ
        return 0
        