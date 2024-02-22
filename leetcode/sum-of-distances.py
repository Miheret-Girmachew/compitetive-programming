class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        hs = {}
        answer = [0]*len(nums)
        for i in range(len(nums)): 
            if nums[i] not in hs:
                hs[nums[i]]=[]
            hs[nums[i]].append(i)
        for num, val in hs.items():
            ss = sum(val)
            pre = 0
            s = len(val)
            p = 0
            for i in val:
                pre += i
                p += 1
                ss -= i
                s-=1
                answer[i] =-pre +  p*i  - s*i + ss
        return answer

        
        