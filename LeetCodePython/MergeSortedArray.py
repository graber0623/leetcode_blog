class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0: return
        p1 = 0
        p2 = 0
        while p1 < len(nums1):
            if nums1[p1] >= nums2[p2]:
                nums1.insert(p1, nums2[p2])
                p1 +=1
                p2 +=1

            else:
                p1 +=1
        

        
