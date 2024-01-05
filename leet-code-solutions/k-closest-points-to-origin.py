"""class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hashh={}
        ans = []
        for i in range(len(points)):
            val=points[i][0]**2 + points[i][1]**2
            if val not in hashh:
                hashh[val]=points[i]
            else:
                hashh[val].append(points[i])
        keyy=list(hashh.keys())
        keyy.sort()
        for i in range(k):
            ans.extend(hashh[keyy[i]])
        return ans"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        nums=[]
        for i in range(len(points)):
            val=(points[i][0]**2)+(points[i][1]**2)
            nums.append([val, points[i]])
        nums.sort(key=lambda x: x[0])

        smallest = [point[1] for point in nums[:k]]

        return(smallest)

            
        