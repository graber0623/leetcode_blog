# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import defaultdict
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True

        d = defaultdict(list)
        i = 0
        while head:
            d[head.val].append(i)
            i += 1
            head = head.next
        print(d)
        for key in list(d.keys()):
            c = d[key]
            if len(c) % 2 == 1:
                if len(c) == 1 and c[0] != i//2:
                    return False
                else:
                    for j in range(int(len(c)//2)):
                        if abs(0 - c[j]) != abs(i-1-c[(-1*j)-1]):
                            return False
                    
                    if c[len(c)//2] != i//2:
                        return False
                    

            else:
                for j in range(int(len(c)/2)):
                    if abs(0 - c[j]) != abs(i-1-c[(-1*j)-1]):
                        return False

        return True 
