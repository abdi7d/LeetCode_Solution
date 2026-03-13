class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = deque()
        dire = deque()
        
        # Initialize queues with indices
        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        
        # Simulate rounds
        while radiant and dire:
            r_index = radiant.popleft()
            d_index = dire.popleft()
            
            # Senator with smaller index bans the other
            if r_index < d_index:
                radiant.append(r_index + n)
            else:
                dire.append(d_index + n)
        
        return "Radiant" if radiant else "Dire"