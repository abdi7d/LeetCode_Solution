class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        map_pw = {}
        map_wp = {}
        
        for p, w in zip(pattern, words):
            if p in map_pw and map_pw[p] != w:
                return False
            if w in map_wp and map_wp[w] != p:
                return False
            
            map_pw[p] = w
            map_wp[w] = p
        
        return True