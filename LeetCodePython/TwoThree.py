from collections import defaultdict
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        nums3 = set(nums3)
        d = defaultdict(int)
        for num in nums1:
            d[num] += 1
        for num in nums2:
            d[num] += 1
        for num in nums3:
            d[num] += 1
        ans = []
        for key in list(d.keys()):
            if d[key] >= 2:
                ans.append(key)

        return ans
