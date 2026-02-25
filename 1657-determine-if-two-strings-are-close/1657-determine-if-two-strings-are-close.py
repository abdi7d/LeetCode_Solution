class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        from collections import Counter

        count1 = Counter(word1)
        count2 = Counter(word2)

        # Condition 1: Same characters
        if set(count1.keys()) != set(count2.keys()):
            return False

        # Condition 2: Same frequency distribution
        if sorted(count1.values()) != sorted(count2.values()):
            return False

        return True