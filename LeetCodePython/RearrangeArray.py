class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos = []
        neg = []

        for i in range(n):
            if nums[i] > 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        ans = []
        for j in range(int(n/2)):
            ans.append(pos[j])
            ans.append(neg[j])

        return ans