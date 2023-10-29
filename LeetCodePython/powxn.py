# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if n == 0:
#             return 1

#         elif n > 0:
#             ans = 1
#             for i in range(n):
#                 ans*=x
#             return ans
#         else:
#             n = -1 * n
#             ans = 1
#             for i in range(n):
#                 ans *= x
#             return 1/ans

class Solution:
    def myPow(self, base: float, exponent: int) -> float:
        if exponent == 0:
            return 1

        result = 1
        is_negative = False

        if exponent < 0:
            is_negative = True
            exponent = -exponent

        while exponent > 0:
            if exponent % 2 == 1:
                result *= base
            base *= base
            exponent //= 2

        return 1 / result if is_negative else result