from collections import defaultdict
class NumberContainers:

    def __init__(self):
        # self.cont = [0] * 1000000000
        self.cont = defaultdict(int)

    def change(self, index: int, number: int) -> None:
        self.cont[index] = number

    def find(self, number: int) -> int:
        for index in sorted(list(self.cont.keys())):
            if self.cont[index] == number:
                return index

        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)