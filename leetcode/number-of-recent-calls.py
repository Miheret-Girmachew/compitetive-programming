class RecentCounter:

    def __init__(self):
        self.recentRequest = deque()
     

    def ping(self, t: int) -> int:
        self.recentRequest.append(t)
        while  self.recentRequest[0]  < t- 3000 :
            self.recentRequest.popleft()
         
        return len(self.recentRequest)
        
        

        


        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)