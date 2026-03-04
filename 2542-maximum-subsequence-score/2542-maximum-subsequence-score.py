class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        import heapq
        
        pairs = sorted(zip(nums2, nums1), reverse=True)
        
        heap = []
        total_sum = 0
        max_score = 0
        
        for num2, num1 in pairs:
            heapq.heappush(heap, num1)
            total_sum += num1
            
            if len(heap) > k:
                total_sum -= heapq.heappop(heap)
            
            if len(heap) == k:
                max_score = max(max_score, total_sum * num2)
        
        return max_score