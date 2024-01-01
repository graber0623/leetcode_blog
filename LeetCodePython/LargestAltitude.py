class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alti = [0]
        for i in range(len(gain)):
            alti.append(alti[-1]+gain[i])

        return max(alti)