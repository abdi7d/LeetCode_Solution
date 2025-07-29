class Solution:
    def possibleStringCount(self, word: str) -> int:
        if not word:
            return 0

        # Store lengths of all groups of repeated characters
        group_lengths = []

        i = 0
        while i < len(word):
            j = i
            while j < len(word) and word[j] == word[i]:
                j += 1

            group_lengths.append(j - i)  # Length of this group
            i = j

        total = 1  # Count the original string as one possibility

        # For each group, add (length - 1) shortened possibilities
        for length in group_lengths:
            total += (length - 1)

        return total


# how it works for "abbccc":
# Step 1: Group the consecutive characters
group_lengths = [1, 2, 3] 

# Step 2: Count how many possibilities we have
length = 1
total = 1 + (1 - 1) = 1

length = 2
total = 1 + (2 - 1) = 2

length = 4
total = 2 + (4 - 1) = 5