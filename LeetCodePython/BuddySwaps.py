from collections import defaultdict
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if sorted(s) != sorted(goal):
            return False

        g_index = defaultdict(list)
        g_counter = defaultdict(int)
        for i in range(len(goal)):
            g_index[goal[i]].append(i)
            g_counter[goal[i]] += 1
        
        for j in range(len(s)):
            goal_indexes = g_index[s[j]]
            for goal_index in goal_indexes:
                if j != goal_index:
                    return True
        
        return False

             