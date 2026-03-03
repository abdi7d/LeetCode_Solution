# class SmallestInfiniteSet:

#     def __init__(self):
        

#     def popSmallest(self) -> int:
        

#     def addBack(self, num: int) -> None:
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

class SmallestInfiniteSet:

    def __init__(self):
        import heapq
        self.current = 1
        self.heap = []
        self.added = set()
        self.heapq = heapq

    def popSmallest(self) -> int:
        if self.heap:
            smallest = self.heapq.heappop(self.heap)
            self.added.remove(smallest)
            return smallest
        else:
            self.current += 1
            return self.current - 1

    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.added:
            self.heapq.heappush(self.heap, num)
            self.added.add(num)