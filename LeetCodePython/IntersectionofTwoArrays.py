from collections import defaultdict
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        ans = set()
        for n in nums2:
            if n in nums1:
                ans.add(n)

        return ans

## 중요 set search complexity is O(1)!!!!!!