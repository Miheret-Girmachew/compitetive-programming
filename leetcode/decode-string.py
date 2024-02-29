class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = []
                while s[i].isdigit():
                    num.append(s[i])
                    i+=1
                stack.append(int("".join(num)))
                i-=1
        
            elif s[i] == "]":
                ss = []
                while stack and stack[-1] != "[":
                   ss.append(stack.pop())
                stack.pop()
                times = int(stack.pop())
                reversee = ss[::-1]
                neww = "".join(reversee)*times
                stack.append(neww)
            else:
                stack.append(s[i])
            i+=1
        return "".join(stack)
           
        
                
                

        