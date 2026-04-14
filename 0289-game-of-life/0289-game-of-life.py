class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        def count_live(r, c):
            directions = [
                (-1,-1), (-1,0), (-1,1),
                (0,-1),         (0,1),
                (1,-1), (1,0), (1,1)
            ]
            
            live = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if abs(board[nr][nc]) == 1:
                        live += 1
            return live
        
        # Step 1: mark transitions
        for i in range(m):
            for j in range(n):
                live_neighbors = count_live(i, j)
                
                if board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = -1  # live → dead
                else:
                    if live_neighbors == 3:
                        board[i][j] = 2   # dead → live
        
        # Step 2: finalize
        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0