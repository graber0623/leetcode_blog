class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        grades = sorted(grades)

        c = 0
        
        while grades:
            c+=1
            if len(grades[:c]) < len(grades[c:]):
                grades = grades[c:]
            else:
                break


        return c


