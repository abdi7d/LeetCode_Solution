import bisect
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        potions.sort()
        n = len(potions)
        result = []
        
        for spell in spells:
            # Minimum potion needed
            target = (success + spell - 1) // spell  # ceil(success / spell)
            
            idx = bisect.bisect_left(potions, target)
            result.append(n - idx)
        
        return result