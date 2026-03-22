# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        prefix = defaultdict(int)
        prefix[0] = 1  # base case
        
        def dfs(node, current_sum):
            if not node:
                return 0
            
            current_sum += node.val
            
            # Check how many paths end here
            count = prefix[current_sum - targetSum]
            
            # Add current sum to map
            prefix[current_sum] += 1
            
            # Recurse
            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)
            
            # Backtrack
            prefix[current_sum] -= 1
            
            return count
        
        return dfs(root, 0)