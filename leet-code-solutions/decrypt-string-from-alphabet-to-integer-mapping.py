class Solution:
    def freqAlphabets(self, s: str) -> str:
        hashh={"1":"a","2":"b","3":"c","4":"d","5":"e","6":"f","7":"g","8":"h","9":"i","10#":"j","11#":"k","12#":"l","13#":"m","14#":"n","15#":"o","16#":"p","17#":"q","18#":"r","19#":"s","20#":"t","21#":"u","22#":"v","23#":"w","24#":"x","25#":"y","26#":"z",}
        
        temp=""
        sn=""
        i=0
        while(i<len(s)):
            if i+2<len(s) and s[i+2]=="#":
                temp=s[i:i+3]
                sn+=hashh[temp]
                i+=3
            else:
                sn+=hashh[s[i]]
                i+=1
        return sn
            
                
                
              
                  
      
        
        