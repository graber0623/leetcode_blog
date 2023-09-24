class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        r = len(colors)-1
        max_length = 0
        for r in range(len(colors)-1, 0, -1):
            if colors[0] != colors[r]:
                max_length = r
                break

        for l in range(len(colors)-1):
            if colors[l] != colors[-1]:
                max_length = max(max_length, len(colors)-1-l)
                break
        return max_length
    
