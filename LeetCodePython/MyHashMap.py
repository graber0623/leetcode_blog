# class MyHashMap: 

#     def __init__(self):
#         self.map = []

#     def put(self, key: int, value: int) -> None:
#         for attribute in self.map:
#             if key == attribute[0]:
#                 self.map.remove(attribute)
#         self.map.append([key, value])
#         return

#     def get(self, key: int) -> int:
#         for attribute in self.map:
#             if key == attribute[0]:
#                 return attribute[1]
#         return -1

#     def remove(self, key: int) -> None:
#         for attribute in self.map:
#             if key == attribute[0]:
#                 self.map.remove(attribute)
class MyHashMap:
    def __init__(self):
        self.size = 10
        self.mp = [[] for _ in range(self.size)]

    def hash(self, key):
        return key % self.size

    def put(self, key, value):
        i = self.hash(key)
        bucket = self.mp[i]

        for idx, pair in enumerate(bucket):
            if pair[0] == key:
                bucket[idx] = (key, value)
                return

        bucket.append((key, value))

    def get(self, key):
        i = self.hash(key)
        bucket = self.mp[i]

        for pair in bucket:
            if pair[0] == key:
                return pair[1]

        return -1

    def remove(self, key):
        i = self.hash(key)
        bucket = self.mp[i]

        for idx, pair in enumerate(bucket):
            if pair[0] == key:
                del bucket[idx]
                return
        
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)