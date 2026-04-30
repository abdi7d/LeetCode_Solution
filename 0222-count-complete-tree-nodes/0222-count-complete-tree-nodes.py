# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # compute left height
        left = root
        left_height = 0
        while left:
            left = left.left
            left_height += 1
        
        # compute right height
        right = root
        right_height = 0
        while right:
            right = right.right
            right_height += 1
        
        # if perfect tree
        if left_height == right_height:
            return (1 << left_height) - 1
        
        # otherwise recurse
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)