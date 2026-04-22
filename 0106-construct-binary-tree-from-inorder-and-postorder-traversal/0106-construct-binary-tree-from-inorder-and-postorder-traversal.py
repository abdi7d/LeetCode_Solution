# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # map value → index
        inorder_map = {val: i for i, val in enumerate(inorder)}
        
        self.post_idx = len(postorder) - 1
        
        def helper(left, right):
            if left > right:
                return None
            
            # root from postorder
            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            
            root = TreeNode(root_val)
            
            mid = inorder_map[root_val]
            
            # build RIGHT first!
            root.right = helper(mid + 1, right)
            root.left = helper(left, mid - 1)
            
            return root
        
        return helper(0, len(inorder) - 1)