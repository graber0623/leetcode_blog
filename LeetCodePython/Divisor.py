class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = (dividend / divisor)
        ans = int(str(ans).split(".")[0])
        if ans < -(2**31):
            ans = -(2**31)
        elif ans > (2**31 - 1):
            ans = (2**31 - 1)

        return ans 


## 2147483647