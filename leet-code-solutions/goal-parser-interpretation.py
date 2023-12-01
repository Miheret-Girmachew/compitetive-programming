class Solution:
    def interpret(self, command: str) -> str:
        s=''
        for i in range(len(command)):
            if command[i]=="(":
                continue
            elif command[i]==')' and command[i-1]=='(':
                s+="o"
            elif command[i]==')' and command[i-1]!='(':
                continue
            else: s+=command[i]
                
        return s
                
                
                
        