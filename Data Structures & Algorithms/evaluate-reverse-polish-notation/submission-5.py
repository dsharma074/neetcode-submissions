class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        out = 0
        import operator 
        dicti = {"+": operator.add,
                "-": operator.sub,
                "*": operator.mul,
                "/": operator.truediv}
        stack = []
        for i,val  in enumerate(tokens):
            if val in dicti:
                b = stack.pop()
                a = stack.pop()
                out = dicti[val](int(a), int(b))
                stack.append(int(out))
            else:
                stack.append(int(val))
        return stack[-1]


            
        