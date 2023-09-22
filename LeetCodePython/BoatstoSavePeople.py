# class Solution:
#     def numRescueBoats(self, people: List[int], limit: int) -> int:
#         people = sorted(people)
#         count = 0
#         on_boat = people[0]
#         for i in range(1,len(people)):
#             if i < len(people)-1:
#                 if on_boat + people[i] < limit:
#                     on_boat += people[i]
#                 elif on_boat + people[i] == limit:
#                     count+=1
#                     on_boat = 0
#                 else:
#                     count+=1
#                     on_boat = people[i]
#             else:
#                 if on_boat + people[i] > limit:
#                     count +=2
#                 else:
#                     count +=1
#         return count

## THIS DOESNT WORK

# class Solution:
#     def numRescueBoats(self, people: List[int], limit: int) -> int:
#         people = sorted(people)
#         count = 0
#         onboard = 0

#         while people:
#             onboard = people[-1]
#             people.pop(-1)
#             pop_index = []
#             for i in range(len(people)-1, -1, -1):
#                 if people[i] <= limit - onboard:
#                     onboard += people[i]
#                     pop_index.append(i)

#             if pop_index:
#                 for j in pop_index:
#                     people.pop(j)

#             count+=1

#         return count
    
    
## I DIDNT GIVE 2 LIMIT PEOPLES FUCK THINK DID IT BETTER
## BUT TIME LIMIT.... DAMM IT

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        count = 0
        onboard = 0

        l = 0
        r = len(people) -1
        while l <= r:
            #print(l , r)

            onboard = people[r]
            if people[l] <= limit - onboard:
                l+=1
            r -=1
            count +=1
            #print(count)
        return count

print(numRescueBoats([3,2,2,1], 3))