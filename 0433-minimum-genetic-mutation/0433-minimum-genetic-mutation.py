class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        
        if endGene not in bank:
            return -1
        
        genes = ['A', 'C', 'G', 'T']
        
        queue = deque([(startGene, 0)])
        visited = set([startGene])
        
        while queue:
            curr, steps = queue.popleft()
            
            if curr == endGene:
                return steps
            
            curr_list = list(curr)
            
            for i in range(len(curr)):
                original = curr_list[i]
                
                for ch in genes:
                    curr_list[i] = ch
                    next_gene = ''.join(curr_list)
                    
                    if next_gene in bank and next_gene not in visited:
                        visited.add(next_gene)
                        queue.append((next_gene, steps + 1))
                
                curr_list[i] = original
        
        return -1