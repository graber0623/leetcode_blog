class Solution:
    def convert(self, s: str, numRows: int) -> str:
      if numRows == 1:
        return s
      ##########
      else:
        zigzag = ["00000000"] + [""] * numRows

        row_position = 1
        for i in range(len(s)):
          sector_position = i%(2*numRows - 2)

          if sector_position >= numRows-1:
            zigzag[row_position] = zigzag[row_position] + s[i]
            row_position -= 1

          elif sector_position < numRows-1:
            zigzag[row_position] = zigzag[row_position] + s[i]
            row_position += 1
          
        return_string = "".join(zigzag[1:])

        return return_string