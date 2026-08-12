class Solution:
    def isValid(self, s: str) -> bool:
        matching = {')':'(', '}': '{', ']':'['}
        stack = []

        for i in s:
            if i in matching:
                opening = stack.pop() if stack else False
                if matching[i] != opening:
                    return False
            else:
                stack.append(i)
        return not stack

        

