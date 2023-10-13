from collections import defaultdict
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)

        for num in nums:
            d[num] +=1

        d = list(sorted(d.items(), key = lambda x : (x[1], -x[0])))
        ans = []
        for part in d:
            for x in range(part[1]):
                ans.append(part[0])

        return ans