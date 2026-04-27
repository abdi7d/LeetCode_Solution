# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, curr):
            if not node:
                return 0
            
            curr = curr * 10 + node.val
            
            # leaf node
            if not node.left and not node.right:
                return curr
            
            return dfs(node.left, curr) + dfs(node.right, curr)
        
        return dfs(root, 0)