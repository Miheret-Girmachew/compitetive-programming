from collections import Counter
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        if len(set(nums))==1:
            return 0
        my_dict = Counter(nums)
        cumm=0
        summ=0
        sortt = sorted(my_dict.items(), reverse = True)
        for i in range(len(sortt)-1):
            summ+=sortt[i][1]
            cumm+=summ
        return cumm 



        




    