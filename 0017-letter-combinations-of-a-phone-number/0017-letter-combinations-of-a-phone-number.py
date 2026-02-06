class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        # Mapping as per standard telephone keypad
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        res = []
        
        def backtrack(index, path):
            # Base case: reached the end of the input string
            if len(path) == len(digits):
                res.append("".join(path))
                return
            
            # Get letters for current digit and recurse
            letters = phone_map[digits[index]]
            for letter in letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()  # Backtrack
        
        backtrack(0, [])
        return res
