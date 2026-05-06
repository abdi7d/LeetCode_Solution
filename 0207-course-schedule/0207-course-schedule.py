class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        # build graph
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        # queue of courses with no prerequisites
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        taken = 0
        
        while queue:
            curr = queue.popleft()
            taken += 1
            
            for nei in graph[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return taken == numCourses