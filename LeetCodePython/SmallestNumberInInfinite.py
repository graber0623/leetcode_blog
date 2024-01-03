class SmallestInfiniteSet:

    def __init__(self):
        self.infi = [1]
        self.removed = set()

    def popSmallest(self) -> int:
        re = self.infi[0]
        self.removed.add(re)
        if len(self.infi) > 1:
            self.infi.pop(0)
        else:
            self.infi[0]+=1

        return re

    def addBack(self, num: int) -> None:
        if num in self.removed:
            self.infi = sorted([num] + self.infi)
            self.removed.remove(num)