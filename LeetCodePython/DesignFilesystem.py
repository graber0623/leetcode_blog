from collections import defaultdict
class FileSystem:

    def __init__(self):
        self.fs = defaultdict(int)

    def createPath(self, path: str, value: int) -> bool:
        if self.fs[path]:
            return False
        
        pathList = path.split('/')[1:]
        if len(pathList) > 1:
            for i in range(1,len(pathList)):
                higherDir = '/'+'/'.join(pathList[:i])
                if not self.fs[higherDir]:
                    return False

        self.fs[path] = value
        return True

    def get(self, path: str) -> int:
        if not self.fs[path]:
            return -1

        return self.fs[path]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)