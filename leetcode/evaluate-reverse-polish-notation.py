class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for op in tokens:
            if op not in ("+", "-", "*", "/"):
                stack.append(int(op))
            elif op in ("+", "-", "*", "/"):
                num2 = stack.pop()
                num1 = stack.pop()  
                if op == "+":
                    result = num1 + num2
                elif op == "-":
                    result = num1 - num2
                elif op == "*":
                    result = num1 * num2
                elif op == "/":
                    result = int(num1 / num2)
                stack.append(result)
        return stack[0]
