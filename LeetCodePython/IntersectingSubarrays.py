from collections import defaultdict
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sub_list1 = self.sublists(nums1)
        sub_list2 = self.sublists(nums2)

        sub_list1 = set(sub_list1)
        sub_list2 = set(sub_list2)
        
        ans = ''
        for sub_list in sub_list1:
            if sub_list in sub_list2 and len(sub_list) > len(ans):
                ans = sub_list
        
        ans = list(ans)
        ans = [int(x) for x in ans]
        return ans
        
    def sublists(self, lst :List[int]) -> List[str]:
        n = len(lst)
        sublists = []
        
        for start in range(n):
            for end in range(start + 1, n + 1):
                sublists.append(''.join([str(x) for x in lst[start:end]]))
        
        return sublists