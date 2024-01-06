class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0

        ans = []
        c = 1

        for i in range(1, len(chars)):
            if chars[i] == chars[i - 1]:
                c += 1
            else:
                ans.append(chars[i - 1])
                if c > 1:
                    ans.extend(list(str(c)))
                c = 1

        # Handling the last character
        ans.append(chars[-1])
        if c > 1:
            ans.extend(list(str(c)))

        return len(ans)
        # ans = []
        # c=1
        # for i in range(1,len(chars)):
        #     if i != len(chars)-1:
        #         if chars[i] == chars[i-1]:
        #             c+=1
        #         else:
        #             ans.append(chars[i-1])
        #             ans.append(str(c))
        #     else:
        #         if chars[i] == chars[i-1]:
        #             c+=1
        #             ans.append(chars[i])
        #             ans.append(str(c))
        #         else:
        #             ans.append(chars[i-1])
        #             ans.append(str(c))

        #             ans.append(chars[i])
        #             ans.append('1')

        # return len(''.join(ans))




        # ans = []
        # c = 1
        # for i in range(1,len(chars)):
        #     if chars[i] == chars[i-1]:
        #         c+=1
        #     else:
        #         ans.append(chars[i-1])
        #         ans.append(str(c))
        # return len(ans)
            