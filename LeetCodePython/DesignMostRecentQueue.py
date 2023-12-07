class MRUQueue:

    def __init__(self, n: int):
        self.que = [i for i in range(1,n+1)]

    def fetch(self, k: int) -> int:
        num = self.que.pop(k-1)
        self.que.append(num)
        return num


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)