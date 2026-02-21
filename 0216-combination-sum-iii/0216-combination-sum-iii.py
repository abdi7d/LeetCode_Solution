class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(start, path, total):
            # If we have k numbers
            if len(path) == k:
                if total == n:
                    result.append(path[:])
                return

            # Try numbers from 'start' to 9
            for num in range(start, 10):
                # Prune if sum exceeds n
                if total + num > n:
                    break

                path.append(num)
                backtrack(num + 1, path, total + num)
                path.pop()

        backtrack(1, [], 0)
        return result