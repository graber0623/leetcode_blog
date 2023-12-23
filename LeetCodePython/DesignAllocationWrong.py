from collections import Counter
class Allocator:

    def __init__(self, n: int):
        self.memory = [0]* n

    def allocate(self, size: int, mID: int) -> int:
        ini = 0
        cnter = Counter(self.memory)
        if size > cnter[0]:
            return -1
        
        for i in range(len(self.memory)):
            if size == 0:
                break
            if self.memory[i] == 0:
                if ini == 0:
                    ini = i 
                self.memory[i] = mID
                size -= 1
        return ini
    


    def free(self, mID: int) -> int:
        c = 0
        for i in range(len(self.memory)):
            if self.memory[i] == mID:
                self.memory[i] = 0
                c+=1

        return c
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)