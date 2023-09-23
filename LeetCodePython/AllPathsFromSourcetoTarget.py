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
    
    
    
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # Initialize an empty list to store the paths
        ans = []
        
        # Define a recursive function to perform DFS
        def dfs(node, path):
            # If the current node is the target node, add the path to the answer list
            if node == len(graph) - 1:
                ans.append(path)
                return
            # Iterate through the neighbors of the current node
            for n in graph[node]:
                # Recursively call the function on the neighbor, passing in a copy of the path list with the neighbor appended
                dfs(n, path + [n])
        
        # Start the DFS search from the source node (node 0)
        dfs(0, [0])
        
        # Return the list of paths
        return ans


