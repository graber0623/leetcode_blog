class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans = []
        n = len(heights)
        # for i in range(n-1):
        #     if heights[i] > max(heights[i+1:]):
        #         ans.append(i)

        # ans.append(n-1)
        # return ans
        heights = heights[::-1]
        ans.append(n-1)
        m = heights[0]
        for i in range(1,n):
            if heights[i] > m:
                ans.append(n-1-i)
            m = max(heights[i], m)

        return ans[::-1]
