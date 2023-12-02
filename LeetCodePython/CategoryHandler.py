# Definition for a category handler.
# class CategoryHandler:
#     def haveSameCategory(self, a: int, b: int) -> bool:
#         pass
class Solution:
    def numberOfCategories(self, n: int, categoryHandler: Optional['CategoryHandler']) -> int:
        c = 0
        for i in range(n):
            if not categoryHandler.haveSameCategory(i, i-1):
                c+=1

        return c

# Definition for a category handler.
# class CategoryHandler:
#     def haveSameCategory(self, a: int, b: int) -> bool:
#         pass
class Solution:
    def numberOfCategories(self, n, categoryHandler):
        res = [0]

        for i in range(1,n):
            val = False
            for j in res:
                if categoryHandler.haveSameCategory(i,j):
                    val = True
                    break

            if not val:
                res.append(i)

        return len(res)