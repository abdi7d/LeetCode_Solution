class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        # convert square number to board coordinates
        def get_position(num):
            row = (num - 1) // n
            col = (num - 1) % n
            
            # reverse direction every row
            if row % 2 == 1:
                col = n - 1 - col
            
            # board counted from bottom
            row = n - 1 - row
            
            return row, col
        
        queue = deque([(1, 0)])  # (square, moves)
        visited = set([1])
        
        while queue:
            square, moves = queue.popleft()
            
            if square == n * n:
                return moves
            
            for next_square in range(square + 1, min(square + 6, n*n) + 1):
                
                r, c = get_position(next_square)
                
                # snake or ladder
                if board[r][c] != -1:
                    destination = board[r][c]
                else:
                    destination = next_square
                
                if destination not in visited:
                    visited.add(destination)
                    queue.append((destination, moves + 1))
        
        return -1