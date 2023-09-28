
def numberOfBeams(bank):
    
    c = 0
    last_sensor_count = 0
    for i in range(len(bank)):
        a = list(bank[i])
        a = [int(x) for x in a]
        current_sensor_count = sum(a)
        print(current_sensor_count, "        ", c)
        if current_sensor_count > 0 and last_sensor_count >0:
            c += current_sensor_count * last_sensor_count
        
        if current_sensor_count > 0:    
            last_sensor_count = current_sensor_count

    return c
print(numberOfBeams(["011001","000000","010100","001000"]))