class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        llist = []
        for num in nums:
            llist.append(str(num))
        for i in range(len(llist)):
            for j in range(i+1, len(llist)):
                if str(llist[i]) + str(llist[j]) > str(llist[j]) + str(llist[i]):
                    continue
                else:
                    llist[i] , llist[j] = llist[j] , llist[i]
        ans = "".join(llist)
        if int(ans)==0:
            return '0'
        return ans

