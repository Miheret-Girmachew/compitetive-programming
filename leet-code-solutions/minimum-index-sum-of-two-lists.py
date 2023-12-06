class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hash1 = {}
        hash2 = {}
        hash3 = {}
        minimum = float("inf")
        ans = []
        
        for i, word in enumerate(list1):
            hash1[word]=i
        #print(hash1)
            
        for j, word in  enumerate(list2):
            hash2[word]=j
        #print(hash2)
            
        for word in list1:
            if word in list2:
                indexx=hash2[word]+hash1[word]
                hash3[word]=indexx
        #print(hash3)
                
        my_list = list(hash3.values())
        minimum = min(my_list)
        #print(minimum)
        
        for key, value in hash3.items():
            if value==minimum:
                ans.append(key) 
        #print(ans)
                
        return ans
        
        
        
        
        
    

                
      
                
            
        
                
        
        