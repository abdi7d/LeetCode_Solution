class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        path = []

        def is_palindrome(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(start: int) -> None:
            if start == len(s):
                res.append(path[:])
                return

            for end in range(start, len(s)):
                if is_palindrome(start, end):
                    path.append(s[start : end + 1])
                    dfs(end + 1)
                    path.pop()

        dfs(0)
        return res
