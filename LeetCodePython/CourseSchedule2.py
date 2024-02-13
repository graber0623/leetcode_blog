from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for l in prerequisites:
            d[l[0]].append(l[1])

        ans = []
        visited = defaultdict(bool)

        def dfs(node):
            if node in visited:
                return visited[node]
            
            visited[node] = True

            for neighbor in d[node]:
                if dfs(neighbor):
                    return True
            
            visited[node] = False
            ans.append(node)
        
        for i in range(numCourses):
            if dfs(i):
                return []
        
        return ans