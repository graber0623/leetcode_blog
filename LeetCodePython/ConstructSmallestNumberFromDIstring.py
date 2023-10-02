class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        numList = [i+1 for i in range(n+1)]
        
        for j in range(n):
            if pattern[j] == "D":
                x = numList[j]
                y = numList[j+1]
                if x < y:
                    numList[j] = y
                    numList[j+1] = x

        
        numList = [str(x) for x in numList]

        return "".join(numList)