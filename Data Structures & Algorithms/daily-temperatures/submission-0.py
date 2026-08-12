class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures) 
        result = [0 for i in range(n)]
        stack = []
        for i in range(n): # basically iterating through the temperatures
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            stack.append(i)
            print(stack)
            print (result)
        return result