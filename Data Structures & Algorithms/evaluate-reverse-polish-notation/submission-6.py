class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        n = len(tokens)
        result = 0
        for i in range(n):
            if tokens[i] not in ["+", "-", "*", "/"]: #"+" or tokens[i] != "-" or tokens[i] != "*" or tokens[i] != "/":
                stack.append(tokens[i])
            else: # it is an operation 
                operation = tokens[i]
                if len(stack) >= 2: 
                    num1 = int(stack.pop())
                    num2 = int(stack.pop())
                    if operation == "+":
                        result = num1 + num2 #stack will be empty and then num2 becomes result
                        stack.append(result)
                    elif operation == "-":
                        result = num2 - num1
                        stack.append(result)
                    elif operation == "*":
                        result = num1 * num2
                        stack.append(result)
                    else:
                        result = int(num2 / num1)
                        stack.append(result)
            print(stack)
        return int(stack.pop())

