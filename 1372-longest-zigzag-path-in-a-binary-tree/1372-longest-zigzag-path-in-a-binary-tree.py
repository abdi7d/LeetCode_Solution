# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_len = 0

        def dfs(node, direction, length):
            if not node:
                return
            
            self.max_len = max(self.max_len, length)

            if direction == "left":
                # Continue zigzag: go right
                dfs(node.right, "right", length + 1)
                # Restart: go left
                dfs(node.left, "left", 1)
            else:
                # Continue zigzag: go left
                dfs(node.left, "left", length + 1)
                # Restart: go right
                dfs(node.right, "right", 1)

        # Start from root in both directions
        dfs(root.left, "left", 1)
        dfs(root.right, "right", 1)

        return self.max_len