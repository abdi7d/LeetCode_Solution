import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        left_heap = []
        right_heap = []
        
        l, r = 0, n - 1
        
        # Fill initial heaps
        for _ in range(candidates):
            if l <= r:
                heapq.heappush(left_heap, costs[l])
                l += 1
            if l <= r:
                heapq.heappush(right_heap, costs[r])
                r -= 1
        
        total = 0
        
        for _ in range(k):
            if not right_heap or (left_heap and left_heap[0] <= right_heap[0]):
                total += heapq.heappop(left_heap)
                if l <= r:
                    heapq.heappush(left_heap, costs[l])
                    l += 1
            else:
                total += heapq.heappop(right_heap)
                if l <= r:
                    heapq.heappush(right_heap, costs[r])
                    r -= 1
        
        return total