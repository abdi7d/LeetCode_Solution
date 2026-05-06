class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        # build graph
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        # start with no prerequisites
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        order = []
        
        while queue:
            curr = queue.popleft()
            order.append(curr)
            
            for nei in graph[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        # check if valid
        return order if len(order) == numCourses else []