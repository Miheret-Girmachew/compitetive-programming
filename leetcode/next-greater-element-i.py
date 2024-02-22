class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hs = {}
        for i in range(len(nums2)):
            hs[nums2[i]]=i

        stack= [0]
        answer = [-1] * len(nums2)
        for i in range(len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                answer[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(i)
        final = [0] * len(nums1)
        for i in range(len(nums1)):
            final[i] = answer[hs[nums1[i]]]
        return final





        