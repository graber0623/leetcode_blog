class MyHashSet:
    def __init__(self):
        self.size = 10
        self.buckets = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        index = self._hash(key)
        if key not in self.buckets[index]:
            self.buckets[index].append(key)

    def remove(self, key: int) -> None:
        index = self._hash(key)
        if key in self.buckets[index]:
            self.buckets[index].remove(key)

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        return key in self.buckets[index]

    def _hash(self, key: int) -> int:
        return key % self.size
    
    def __str__(self):
        result = ""
        for i, bucket in enumerate(self.buckets):
            result += f"Bucket {i}: {bucket}\n"
        return result
    
a = MyHashSet()
print(a)

a.add(1)
print(a)
a.add(3)
print(a)



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)