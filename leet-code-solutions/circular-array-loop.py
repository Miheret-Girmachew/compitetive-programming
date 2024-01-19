class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            sn=set()
            j=i
            while True:
                summ=(j+nums[j])%len(nums)
                if j==i:
                    sn.add(i)

                if summ==j:
                    break
                elif summ in sn:
                    return True
                else:
                    if nums[summ]*nums[j]<0:
                        break
                    else:
                        j=summ
                        sn.add(j)

        return False