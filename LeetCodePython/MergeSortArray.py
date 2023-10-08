def merge(nums1, m, nums2, n):
    nums1 = nums1[:m]+nums2[:n]
    nums1 = sorted(nums1)
    print(nums1)
    
merge([1,2,3,0,0,0], 3, [2,4,6],3)