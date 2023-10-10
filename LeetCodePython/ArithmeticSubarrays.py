class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        m = len(l)
        ans = []
        for i in range(m):
            que = sorted(nums[l[i]:r[i]+1])
            diff = que[0]-que[1]
            before = len(ans)
            for j in range(1, len(que)-1):
                if que[j] - que[j+1] != diff:
                    ans.append(False)
                    break
            after = len(ans)
            if before == after:
                ans.append(True)

        return ans
    
print(Solution.checkArithmeticSubarrays(Solution, nums = [4,6,5,9,3,7], l = [0,0,2], r=[2,3,5] ))