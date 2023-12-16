class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        water = capacity
        step = 0
        for i in range(len(plants)):
            step +=1 
            if plants[i] > water:
                step += 2*i
                water = capacity
            
            water -= plants[i]

        return step