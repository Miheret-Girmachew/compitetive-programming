class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        new = path.split('/')
        for i in new:
            if i == '' or i == '.':
                continue
            elif stack != [] and i == "..":
                stack.pop()
            if i != "..": 
                stack.append(i)
                
        return "/"+('/'.join(stack))
             
            
            
            
            
    