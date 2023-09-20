## FROM A GITHUB SOLUTION
def minMeetingRooms(intervals):
    intervals = sorted(intervals)
    if len(intervals) == 1:
        return 1
        
    end_time = []
    for s,e in intervals:

        if len(end_time) == 0:
            end_time.append(e)
            continue
        soonest_e = end_time[0]
        if soonest_e <= s:
            end_time.pop(0)
            end_time.append(e)
            end_time = sorted(end_time)
        elif soonest_e > s:
            end_time.append(e)
            end_time = sorted(end_time)
            
    return len(end_time)
            
test = [[0,30],[5,10],[15,20]]
print(minMeetingRooms(test))