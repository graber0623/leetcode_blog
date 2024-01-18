# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        med = n//2
        bot = 0
        top = n
        
        while bot < top:
            
            if guess(med) == 0:
                break
            
            if guess(med) == -1:
                top = med - 1
                med = (top+bot)//2
            elif guess(med) == 1:
                bot = med + 1
                med = (top+bot)//2
        
        return med