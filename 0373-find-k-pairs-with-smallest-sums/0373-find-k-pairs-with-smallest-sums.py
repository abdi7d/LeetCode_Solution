class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        if not nums1 or not nums2:
            return []
        
        heap = []
        result = []
        
        # initialize heap with first column
        for i in range(min(k, len(nums1))):
            heapq.heappush(
                heap,
                (nums1[i] + nums2[0], i, 0)
            )
        
        while heap and len(result) < k:
            
            total, i, j = heapq.heappop(heap)
            
            result.append([nums1[i], nums2[j]])
            
            # move right in nums2
            if j + 1 < len(nums2):
                
                heapq.heappush(
                    heap,
                    (
                        nums1[i] + nums2[j + 1],
                        i,
                        j + 1
                    )
                )
        
        return result