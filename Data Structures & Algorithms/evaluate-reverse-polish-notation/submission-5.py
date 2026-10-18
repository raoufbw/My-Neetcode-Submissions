class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        stack = []
        for e in tokens:
            if e == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(b+a)
            elif e == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif e == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(b*a)
            elif e == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(e))
        return stack[-1]



