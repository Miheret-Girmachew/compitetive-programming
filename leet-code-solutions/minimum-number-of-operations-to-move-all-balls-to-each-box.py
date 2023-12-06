class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        steps=[]
        for i in range(len(boxes)):
            summ=0
            for j in range(len(boxes)):
                if boxes[j] != "0":
                    summ+= abs(i-j)
            steps.append(summ)
        return steps
        