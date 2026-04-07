class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        
        while i < len(words):
            # Step 1: find words for this line
            line_words = []
            line_len = 0
            
            while i < len(words) and line_len + len(words[i]) + len(line_words) <= maxWidth:
                line_words.append(words[i])
                line_len += len(words[i])
                i += 1
            
            # Step 2: build the line
            spaces = maxWidth - line_len
            gaps = len(line_words) - 1
            
            # Last line or single word
            if i == len(words) or gaps == 0:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            else:
                space = spaces // gaps
                extra = spaces % gaps
                
                line = ""
                for j in range(gaps):
                    line += line_words[j]
                    line += " " * (space + (1 if j < extra else 0))
                line += line_words[-1]
            
            res.append(line)
        
        return res