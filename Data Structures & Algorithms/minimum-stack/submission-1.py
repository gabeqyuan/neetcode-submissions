class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0 or val <= self.minStack[-1]:
            self.minStack.append(val)
        else: 
            self.minStack.append(self.minStack[-1])


    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
    def top(self) -> int:
        val = self.stack[-1]
        return val

    def getMin(self) -> int:
        minVal = self.minStack[-1]
        return minVal

