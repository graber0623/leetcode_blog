from collections import defaultdict
class Skiplist:

    def __init__(self):
        self.skipList = defaultdict(int)

    def search(self, target: int) -> bool:
        if self.skipList[target] > 0:
            return True
        return False

    def add(self, num: int) -> None:
        self.skipList[num] += 1

    def erase(self, num: int) -> bool:
        if self.skipList[num] > 0:
            self.skipList[num]-= 1
            return True
        return False


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)