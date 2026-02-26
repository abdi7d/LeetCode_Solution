class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        from collections import Counter

        freq = Counter(arr)            # Count occurrences of each number
        occurrences = list(freq.values())
        return len(occurrences) == len(set(occurrences))