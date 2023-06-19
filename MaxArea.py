height = [1,8,6,2,5,4,8,3,7]


def maxArea(height):
    l = 0
    r = len(height) - 1
    Area = 0
    h = max(height)
    while l <= r:
        cArea = min(height[l], height[r]) * (r - l)
        Area = max(Area, cArea)
        if height[l] < height[r]:
            l += 1
        elif height[l] > height[r]:
            r -= 1
        else:
            l, r = l + 1, r - 1
        if (r - l) * h <= Area:
            break
    return Area

print(maxArea(height))