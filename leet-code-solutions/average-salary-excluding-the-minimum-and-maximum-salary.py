class Solution:
    def average(self, salary: List[int]) -> float:
        maximum=max(salary)
        minimum=min(salary)
        new=[]
        for num in salary:
            if num==maximum or num==minimum:
                continue
            else:
                new.append(num)
        return sum(new)/len(new)