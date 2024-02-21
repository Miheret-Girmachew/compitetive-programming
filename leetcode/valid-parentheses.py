class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == "[" or s[i] == "(" or s[i] =="{":
                stack.append(s[i])
                
            else:
                if len(stack)==0:
                    return False
                if s[i] == "}" and stack[-1]!="{":
                    return False
                elif s[i] == "]" and stack[-1]!="[":
                     return False
                elif s[i] == ")" and stack[-1]!="(":
                    return False
                else:
                    stack.pop()
        if stack:
            return False
        return True