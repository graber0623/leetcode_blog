def gasStation(gas, cost): ## TIME LIMIT EXCEEDED
    for i in range(len(gas)):
        new_gas = gas[i:] + gas[:i]
        new_cost = cost[i:] + cost[:i]
        j = 0
        gas_left = 0
        while j < len(new_gas):
            gas_left += new_gas[j]
            gas_left -= new_cost[j]
            
            if gas_left < 0:
                break
            j += 1
            if j == len(new_gas):
                return i
        
    return -1
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

print(gasStation(gas, cost))
# g = [1,2,3,4,5]
# for i in range(len(g)):
#     new_gas = g[i:] + g[:i]
#     print(new_gas)