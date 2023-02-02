from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        add = lambda a,b: a+b
        sub = lambda a,b: b-a
        mult = lambda a,b: a*b
        div = lambda a,b: int(b/a)
        operators = {"+":add, "-":sub, "*":mult, "/":div}
        stack = [int(tokens[0]), int(tokens[1])]
        result = 0
        for i in range(2, len(tokens)):
            if tokens[i] in operators:
                result = operators[tokens[i]](stack.pop(), stack.pop())
                stack.append(result)
            else:
                stack.append(int(tokens[i]))
        return stack[-1]