class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.total=[0]
        self.summ=0
        for num in nums:
            self.summ+=num
            self.total.append(self.summ)

    def sumRange(self, left: int, right: int) -> int:
        print(self.total[right])

        return self.total[right+1]-self.total[left]

       


        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)