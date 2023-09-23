# # class Solution:
# #     def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
# #         path = 0
# #         target = len(graph)-1
# #         def dfs(node):
# #             nonlocal path, target
# #             for next_index in node:
# #                 if next_index == target:
# #                     path+=1
# #                 else:
# #                     dfs(graph[next_index])
        
# #         dfs(graph[0])

# #         return path
# ### VERY WRONG

# a = []

# if a:
#     print("s")
    
# else:
#     print("f")

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        paths = []
        target = len(graph) - 1

        def dfs(node, single, last_index):

            single.append(last_index)

            if last_index == target:
                paths.append(single.copy())
                return
            if not node:
                return
            
            for next_index in node:
                if next_index in single:
                    continue
                else:
                    dfs(graph[next_index], single, next_index)
                    single.pop()


        dfs(graph[0], [], 0)
        return paths