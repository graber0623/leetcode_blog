from collections import defaultdict
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for pair in adjacentPairs:
            d[pair[0]].append(pair[1])
            d[pair[1]].append(pair[0])

        ans = [adjacentPairs[0][0]]

        n = len(adjacentPairs)
        while len(ans) < n:
            new_point = ans[-1]
            print(ans)
            print(new_point)
            ans = list(set(ans + d[new_point]))
        
        return ans



        ans = []
        def dfs(visited):
            nonlocal ans
            lastNum = visited[-1]
            print(visited)
            print(lastNum)
            if not d[lastNum]:
                if len(ans) < len(visited):
                    ans = visited
                return

            for newKey in d[lastNum]:
                if newKey in visited:
                    continue
                
                visited.append(newKey)
                dfs(visited)
                visited.pop()

        for key in d.keys():
            dfs([key])
        return ans
                
                
                
