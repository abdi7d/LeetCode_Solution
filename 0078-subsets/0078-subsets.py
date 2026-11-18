class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        subset = []

        def dfs(i: int) -> None:
            if i == len(nums):
                res.append(subset.copy())
                return

            # Include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # Exclude nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res
