class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        c = Counter(s)
        mono = []
        setMono = set()
        for i in range(len(s)):
            if not mono:
                mono.append(s[i])
                setMono.add(s[i])
            else:
                if s[i] in setMono:
                    c[s[i]]-=1
                    continue
                while mono and mono[-1]>s[i] and c[mono[-1]]>1:
                    c[mono[-1]]-=1
                    setMono.remove(mono.pop())
  
                mono.append(s[i])
                setMono.add(s[i])
        
        
        return "".join(mono)


       