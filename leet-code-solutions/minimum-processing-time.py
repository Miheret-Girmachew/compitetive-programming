class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()
        print(tasks)
        ans = []
        l=0
        i = 0
        while(i<len(tasks)):
            maxx = max(tasks[i:i+4])
            print(tasks[i:i+4])
            ans.append(maxx + processorTime[l])
            print()
            print(maxx + processorTime[l])
            l+=1
            i+=4
        return max(ans)
            
    
        
        