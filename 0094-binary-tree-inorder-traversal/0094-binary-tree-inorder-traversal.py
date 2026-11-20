# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        res = []
        
        def dfs(node):
            if not node:
                return
            dfs(node.left)       # 1. Visit left subtree
            res.append(node.val) # 2. Process current node
            dfs(node.right)      # 3. Visit right subtree
            
        dfs(root)
        return res
