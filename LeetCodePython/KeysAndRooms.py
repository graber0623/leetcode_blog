class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = [0] * len(rooms)
        def dfs(key):
            nonlocal visited
            if visited[key] == 1:
                return

            visited[key] = 1
            for new_key in rooms[key]:
                dfs(new_key)
        dfs(0)

        if 0 in visited:
            return False
        else:
            return True