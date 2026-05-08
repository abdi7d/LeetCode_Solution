# class WordDictionary:

#     def __init__(self):
        

#     def addWord(self, word: str) -> None:
        

#     def search(self, word: str) -> bool:
        
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            
            node = node.children[ch]
        
        node.is_end = True

    def search(self, word: str) -> bool:
        
        def dfs(j, node):
            
            for i in range(j, len(word)):
                ch = word[i]
                
                # wildcard
                if ch == '.':
                    for child in node.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                
                # normal character
                if ch not in node.children:
                    return False
                
                node = node.children[ch]
            
            return node.is_end
        
        return dfs(0, self.root)