from collections import defaultdict
def isHappy(n):
    d = defaultdict(int)

    def dfs(x):
        if d[x]:
            return False
        else:
            d[x]=1
            #####
            x_list = list(str(x))
            new_num = sum([int(digit) ** 2 for digit in x_list])
            print(new_num)
            if new_num == 1:
                return True
            else:
                return dfs(new_num)
    return dfs(n)

print(isHappy(19))