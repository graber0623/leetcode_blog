from collections import defaultdict
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        d = defaultdict(list)
        f = defaultdict(int)

        for order in orders:
            ## order[1] = table name, order[2] is food name
            d[order[1]].append(order[2])
            f[order[2]] = 0

        d = dict(sorted(d.items(), key = lambda x: int(x[0]))) 
        f = dict(sorted(f.items()))
        ans = [['Table'] + list(f.keys())]

        for table_number in d.keys():
            foods = f.copy() ## Empty Menu with Zeros
            for food in d[table_number]:
                foods[food]+=1

            ans.append([table_number] + [str(x) for x in list(foods.values())])

        return ans


