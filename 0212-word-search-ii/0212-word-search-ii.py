class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        
        # Build Trie
        for word in words:
            node = root
            
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                
                node = node.children[ch]
            
            node.word = word
        
        rows, cols = len(board), len(board[0])
        result = []
        
        def dfs(r, c, node):
            ch = board[r][c]
            
            if ch not in node.children:
                return
            
            next_node = node.children[ch]
            
            # word found
            if next_node.word:
                result.append(next_node.word)
                next_node.word = None   # avoid duplicates
            
            # mark visited
            board[r][c] = '#'
            
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if (0 <= nr < rows and
                    0 <= nc < cols and
                    board[nr][nc] != '#'):
                    
                    dfs(nr, nc, next_node)
            
            # restore
            board[r][c] = ch
        
        # start DFS from every cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        
        return result