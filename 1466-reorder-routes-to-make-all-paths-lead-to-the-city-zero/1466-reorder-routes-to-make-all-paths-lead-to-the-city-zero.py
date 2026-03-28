from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)

        # Build graph
        for a, b in connections:
            graph[a].append((b, 1))  # original direction (needs reversal)
            graph[b].append((a, 0))  # reverse direction (correct)

        visited = set()

        def dfs(city):
            visited.add(city)
            changes = 0

            for neighbor, needs_reversal in graph[city]:
                if neighbor not in visited:
                    changes += needs_reversal
                    changes += dfs(neighbor)

            return changes

        return dfs(0)