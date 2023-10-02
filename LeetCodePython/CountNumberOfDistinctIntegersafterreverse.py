class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        c = 0
        new_num = nums.copy()
        for num in nums:
            str_num = str(num)
            if len(str_num) == 1:
                continue
            else:
                new_num.append(int(str_num[::-1]))
        
        re = set(new_num)
    
        return len(re)