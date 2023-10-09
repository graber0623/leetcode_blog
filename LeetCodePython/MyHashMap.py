class MyHashMap:

    def __init__(self):
        self.map = []

    def put(self, key: int, value: int) -> None:
        for attribute in self.map:
            if key == attribute[0]:
                self.map.remove(attribute)
        self.map.append([key, value])
        return

    def get(self, key: int) -> int:
        for attribute in self.map:
            if key == attribute[0]:
                return attribute[1]
        return -1

    def remove(self, key: int) -> None:
        for attribute in self.map:
            if key == attribute[0]:
                self.map.remove(attribute)
        
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)