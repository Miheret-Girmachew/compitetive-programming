class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # new = citations[::-1]
        # hs = {}
        # add = 0
        # for n in citations:
        #     add += 1
        #     hs[n]= add
        # print(hs)
        # l  = 0
        # r  = len(citations)-1
        # while l<=r:
        #     print(l,r)
        #     mid = (l+r)//2
        #     if hs[citations[mid]]<=citations[mid]:
        #         r =mid-1
        #     else:
        #         l = mid+1
        # print(l)
        
        # return citations[l]

        n = len(citations)
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if citations[mid] >= n - mid:
                r = mid - 1
            else:
                l = mid + 1
        return n - l