class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)

        # Build graph
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1/val))

        def dfs(start, end, visited):
            if start not in graph:
                return -1.0
            
            if start == end:
                return 1.0
            
            visited.add(start)

            for neighbor, weight in graph[start]:
                if neighbor in visited:
                    continue
                result = dfs(neighbor, end, visited)
                if result != -1.0:
                    return result * weight

            return -1.0

        res = []

        for a, b in queries:
            res.append(dfs(a, b, set()))

        return res