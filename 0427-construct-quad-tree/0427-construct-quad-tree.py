"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        n = len(grid)
        
        def build(r, c, size):
            
            # check if all values same
            same = True
            first = grid[r][c]
            
            for i in range(r, r + size):
                for j in range(c, c + size):
                    
                    if grid[i][j] != first:
                        same = False
                        break
                
                if not same:
                    break
            
            # leaf node
            if same:
                return Node(
                    first,
                    True,
                    None,
                    None,
                    None,
                    None
                )
            
            half = size // 2
            
            return Node(
                1,
                False,
                
                build(r, c, half),                    # topLeft
                build(r, c + half, half),             # topRight
                build(r + half, c, half),             # bottomLeft
                build(r + half, c + half, half)       # bottomRight
            )
        
        return build(0, 0, n)