class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2, reverse = True)

        sum = 0
        for i in range(len(nums1)):
            sum += nums1[i] * nums2[i]

        return sum