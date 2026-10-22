class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        stack = []
        for i in range(n):
            if not stack:
                stack.append((temperatures[i],i))
            else:
                while stack and stack[-1][0] < temperatures[i]:
                    t, ind = stack[-1]
                    res[ind] = i - ind
                    stack.pop() 
                stack.append((temperatures[i],i))
        return res