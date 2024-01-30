from collections import defaultdict
class TwoSum:

    def __init__(self):
        #self.l = set()
        #self.d = defaultdict(int)
        self.l = []
    def add(self, number: int) -> None:
        #self.l.add(number)
        #self.d[number]+=1
        self.l.append(number)
    def find(self, value: int) -> bool:
        d = defaultdict(int)
        for i in range(len(self.l)):
            d[(value - self.l[i])] +=1
        
        for num in self.l:
            if d[num]:
                return True
            else:
                return False
        # re = False
        # for key in list(self.d.keys()):
        #     if value - key == key:
        #         if self.d[key] >= 2:
        #             re = True
        #         else:
        #             continue
        #     elif self.d[value-key]:
        #         re = True
        # return re
# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)