class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ans = []
        hashh = {}
        for i in range(len(names)):
            hashh[heights[i]]=names[i]
        heights.sort(reverse=True)
        for i in range(len(heights)):
            ans.append(hashh[heights[i]])
        return ans 