class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = []
        ans = []
        for i in range(len(intervals)):
            starts.append((intervals[i][0],i))
        starts.sort()
        print(starts)
        for i in range(len(intervals)):
            l = 0
            r = len(intervals)-1
            val = -1
            while l<= r:
                mid = (l+r)//2
                if intervals[i][1] <= starts[mid][0]:
                    r = mid-1
                    val = starts[mid][1]
                else:
                    l = mid+1
            ans.append(val)
        return ans 
        
            
            
            
        