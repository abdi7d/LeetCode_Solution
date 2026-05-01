# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        queue = deque([root])
        left_to_right = True
        
        while queue:
            level = []
            size = len(queue)
            
            for _ in range(size):
                node = queue.popleft()
                
                if left_to_right:
                    level.append(node.val)
                else:
                    level.insert(0, node.val)  # reverse direction
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(level)
            left_to_right = not left_to_right
        
        return res