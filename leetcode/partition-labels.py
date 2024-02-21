class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashlast={}

        for i, last in enumerate(s):
            hashlast[last]=i
        size=0
        last1=0
        result=[]
        for i, last in enumerate(s):
            size+=1
            last1= max(hashlast[last], last1)
            if i == last1:
                result.append(size)
                size=0
        return result

        