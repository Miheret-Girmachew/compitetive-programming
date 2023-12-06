class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        hold= capacity
        step=0
        for i in range(len(plants)):
            if hold >= plants[i]:
                hold=hold-plants[i]
                step+=1
            else:
                step+=2*i+1
                hold=capacity
                hold=hold-plants[i]
        return step
            
        