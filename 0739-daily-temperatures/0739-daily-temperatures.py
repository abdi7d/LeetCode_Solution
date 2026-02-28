class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)
        ans = [0] * n  # Initialize with 0s for days that never see a warmer day
        stack = []     # Stores indices

        for i, temp in enumerate(temperatures):
            # While current temp is warmer than the temp at the top index
            while stack and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
            
        return ans
