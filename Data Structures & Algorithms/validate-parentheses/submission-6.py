class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stack = []
        if s == '':
            return True
        for i in range(n):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])

            if s[i] == ')':
                if not stack:
                    return False
                else: 
                    opening = stack.pop()
                if opening != '(':
                    return False
            elif s[i] == ']':
                if not stack:
                    return False
                else: 
                    opening = stack.pop()
                if opening != '[':
                    return False
                else:
                    continue
            elif  s[i] == '}':
                if not stack:
                    return False
                else: 
                    opening = stack.pop()
                if opening != '{':
                    return False
                else:
                    continue
        if len(stack) == 0:
            return True
        else:
            return False


