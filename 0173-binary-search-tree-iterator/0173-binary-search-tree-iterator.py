# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class BSTIterator:

#     def __init__(self, root: Optional[TreeNode]):
        

#     def next(self) -> int:
        

#     def hasNext(self) -> bool:
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:

    def __init__(self, root):
        self.stack = []
        self._pushLeft(root)
    
    def _pushLeft(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        
        # after visiting node, go to right subtree
        if node.right:
            self._pushLeft(node.right)
        
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0