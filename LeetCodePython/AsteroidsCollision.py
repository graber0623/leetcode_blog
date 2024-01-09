class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        l = len(asteroids)
        i = 1
        while i < len(asteroids):
            if asteroids[i] < 0 and asteroids[i-1] > 0:
                if abs(asteroids[i]) > abs(asteroids[i-1]):
                    asteroids.pop(i-1)
                    i-=1
                    if i < 1:
                        i =1
                elif abs(asteroids[i]) == abs(asteroids[i-1]):
                    asteroids.pop(i)
                    asteroids.pop(i-1)
                    i-=2
                    if i < 1:
                        i =1
                else:
                    asteroids.pop(i)
                    i-=1
                    if i < 1:
                        i =1
            else:
                i+=1
        return asteroids
                