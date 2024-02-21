class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])
        brust = 1
        finish = points[0][1]
        for i in range(1, len(points)):
            if points[i][0]>finish:
                brust += 1
                finish = points[i][1]
        return brust               
        