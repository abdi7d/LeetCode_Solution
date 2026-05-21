# class MedianFinder:

#     def __init__(self):
        

#     def addNum(self, num: int) -> None:
        

#     def findMedian(self) -> float:
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

import heapq

class MedianFinder:

    def __init__(self):
        
        # max heap (store negatives)
        self.small = []
        
        # min heap
        self.large = []

    def addNum(self, num: int) -> None:
        
        # push into max heap
        heapq.heappush(self.small, -num)
        
        # ensure ordering:
        # max(small) <= min(large)
        if (
            self.small and self.large and
            (-self.small[0] > self.large[0])
        ):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # balance sizes
        if len(self.small) > len(self.large) + 1:
            
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.large) > len(self.small) + 1:
            
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        
        # odd count
        if len(self.small) > len(self.large):
            return -self.small[0]
        
        if len(self.large) > len(self.small):
            return self.large[0]
        
        # even count
        return (
            -self.small[0] + self.large[0]
        ) / 2