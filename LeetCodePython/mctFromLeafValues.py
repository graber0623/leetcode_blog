class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        while len(arr)>1:
            index = arr.index(min(arr))
            if 0 < index < len(arr)-1:
                res += arr[index] * min(arr[index-1], arr[index+1])

            else:
                if index == 0:
                    res += arr[index] * arr[index+1]
                elif index == len(arr)-1:
                    res += arr[index] * arr[index-1]
            print(arr[index], res)
            arr.pop(index)
            print(arr)

        return res