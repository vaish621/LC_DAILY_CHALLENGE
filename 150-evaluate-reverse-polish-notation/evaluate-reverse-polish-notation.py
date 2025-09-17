from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = ["+", "-", "*", "/"]

        for token in tokens:
            if token in op:
                p1 = stack.pop()
                p2 = stack.pop()
                
                if token == "+":
                    stack.append(p2 + p1)
                elif token == "-":
                    stack.append(p2 - p1)
                elif token == "*":
                    stack.append(p2 * p1)
                else: 
                    stack.append(int(p2 / p1))  
            else:
                stack.append(int(token))

        return stack[-1]
