from collections import defaultdict
# class Solution:
#     def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
#         dic = defaultdict(list)
#         for a, b in edges:
#             dic[a].append(b)
#             dic[b].append(a)

#         def dfs(x, y):
#             if not dic[x]:
#                 return False
#             if y in dic[x]:
#                 return True
            
#             for new_x in dic[x]:
#                 dfs(new_x, y)
            
#         return dfs(source, destination)

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dic = defaultdict(list)
        for a, b in edges:
            dic[a].append(b)
            dic[b].append(a)
        
        visited = [False] * n

        def dfs(x, y, visited):
            if x == y:
                return True
            
            visited[x] = True
            if y in dic[x]:
                return True
            
            for new_x in dic[x]:
                if visited[new_x] == False:
                    #dfs(new_x, y, visited)
                    if dfs(new_x, y, visited):
                        return True
            
            return False
        
        return dfs(source, destination, visited)