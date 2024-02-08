from collections import defaultdict
class RandomizedSet:

    def __init__(self):
        self.set = defaultdict(int)

    def insert(self, val: int) -> bool:
        if self.set[val]:
            return False
        else:
            self.set[val] += 1
            return True


    def remove(self, val: int) -> bool:
        if self.set[val]:
            self.set.pop(val)
            return True
        else:
            return False


    def getRandom(self) -> int:
        keys = list(self.set.keys())
        return keys[0]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()