class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        projects = list(zip(capital, profits))
        projects.sort()
        
        maxHeap = []
        i = 0
        
        for _ in range(k):
            
            # add all affordable projects
            while i < len(projects) and projects[i][0] <= w:
                
                # negative for max heap
                heapq.heappush(
                    maxHeap,
                    -projects[i][1]
                )
                
                i += 1
            
            # no affordable projects
            if not maxHeap:
                break
            
            # choose highest profit
            w += -heapq.heappop(maxHeap)
        
        return w