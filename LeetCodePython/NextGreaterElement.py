class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        d = defaultdict(int)
        for i, num in enumerate(nums2):
            d[num] = i
        
        for num in nums1:
            new = nums2[d[num]:]
            l = len(ans)
            for left in new:
                if left > num:
                    ans.append(left)
                    break
            if len(ans) == l:
                ans.append(-1)

        return ans