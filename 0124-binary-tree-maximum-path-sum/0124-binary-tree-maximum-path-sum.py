# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        
        def dfs(node):
            if not node:
                return 0
            
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            
            # path passing through this node
            current = node.val + left + right
            
            self.max_sum = max(self.max_sum, current)
            
            # return one side
            return node.val + max(left, right)
        
        dfs(root)
        return self.max_sum