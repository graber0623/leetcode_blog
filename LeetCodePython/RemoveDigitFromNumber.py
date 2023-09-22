class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_number = 0
        for i in range(len(number)):
            if i == len(number)-1:
                if number[i] == digit:
                    max_number = max(max_number, int(number[:i]))
            else:
                if number[i] == digit:
                    max_number=max(max_number, int(number[:i] + number[i+1:]))
        return str(max_number)