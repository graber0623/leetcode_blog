# def cs(numCourses, prerequisites): ## WRONG!!! circular it is ok until hash map
#     d = {}
#     for pre in prerequisites:
#         if pre[0] in d:
#             d[pre[0]].append(pre[1])
#         else:
#             d[pre[0]] = [pre[1]]

#     for i, set in enumerate(d.items()):
#         key = set[0]
#         list_values = set[1]
#         for value in list_values:
#             if value in d:
#                 if key in d[value]:
#                     return "false"
            
#     return "true"

# print(cs(2, [[1,0],[0,1]]))

# a = {1: [0, 1], 0: [1, 1]}

def cs(numCourses, prerequisites): 
    d = {}
    for pre in prerequisites:
        if pre[0] in d:
            d[pre[0]].append(pre[1])
        else:
            d[pre[0]] = [pre[1]]
            
    taken = [] ## MUST CHECK THIS FIRST
    
    def dfs(course):
        if not d[course]:
            return True
        if course in taken:
            return False
        
        taken.append(course)
        
        for next_course in d[course]:
            if dfs(next_course) == False:
                return False
        
        d[course] = []
        
        return True
    
    
    for i in range(numCourses):
        if dfs(i) == False:
            return False
        
    return True
        
        

## I REALLY DONT UNDERSTAND THIS ONE