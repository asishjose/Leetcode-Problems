class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        map = {
            "*": lambda x, y: x * y,
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "/": lambda x, y: x / y
        }

        for i in tokens:
            if i in map:
                x = stack[-2]
                y = stack[-1]
                stack.pop()
                stack.pop()
                stack.append(int(map[i](x, y)))
            else:
                stack.append(int(i))
        
        return stack[0]
            