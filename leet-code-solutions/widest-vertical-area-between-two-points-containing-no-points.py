class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_list=[]
        for i in range(len(points)):
            x_list.append(points[i][0])
        x_list.sort()
        wide=0
        for i in range(len(points)-1):
            val=x_list[i+1] - x_list[i]
            wide=max(val,wide)
        return wide
        