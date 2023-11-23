class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        cl= list(colors)
        i = 1
        remove_count = 0

        while i < len(cl)-1:

            if cl[i-1] == cl[i] and cl[i] == cl[i+1]:
                remove_count +=1
                cl.pop(i)
            
            else:
                i+=1

        if remove_count % 2 == 1:
            return True
        else:
            return False


## READ THE QUESTION!