class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)-1
        found = False
        while l<=r:
            mid = (l+r)//2
            if matrix[mid][-1]<target:
                l = mid+1
            elif matrix[mid][-1]>target:
                if matrix[mid][0]<target:
                    bl = 0
                    br = len(matrix[mid])-1
                    while bl<=br:
                        bmid = (bl+br)//2
                        if matrix[mid][bmid]>target:
                            br = bmid-1
                        elif matrix[mid][bmid]<target:
                            bl = bmid+1
                        else:
                            found = True
                            return True
                    if found == False:
                        return False
                elif matrix[mid][0]==target:
                    return True
                else:
                    r = mid-1
            else:
                return True
        return False
                


        