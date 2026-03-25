class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        
        queue = deque([(entrance[0], entrance[1], 0)])  # (row, col, steps)
        visited = set([(entrance[0], entrance[1])])
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while queue:
            r, c, steps = queue.popleft()
            
            # Check if it's an exit (not entrance)
            if (r, c) != (entrance[0], entrance[1]) and (r == 0 or r == m-1 or c == 0 or c == n-1):
                return steps
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == '.' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, steps + 1))
        
        return -1