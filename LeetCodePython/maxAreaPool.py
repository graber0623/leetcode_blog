a = [1,7,6,2,5,4,8,3,7]
def maxArea(height):
    max_area = 0
    l = 0
    r = len(height) - 1
    while l < r:
        print(l,r)
        area = (r - l) * min(height[r], height[l])
        max_area = max(max_area, area)
        print(area, "        ",max_area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_area
print(maxArea(a))