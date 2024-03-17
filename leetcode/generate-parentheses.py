class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        temp = []
        ans= []
        def back(op, cl):
            if op==cl==n:
                ans.append("".join(temp))
                return
            if op<n:
                temp.append("(")
                back(op+1, cl)
                temp.pop()
            if cl<op:
                temp.append(")")
                back(op,cl+1)
                temp.pop()
        back(0,0)
        return ans
        