# 2418. Sort the People
def sortPeople(names, heights):
    n = len(heights)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if heights[j] < heights[j + 1]:
                heights[j], heights[j + 1] = heights[j + 1], heights[j]
                names[j], names[j + 1] = names[j + 1], names[j]

    return names
    
    
# names = ["Mary","John","Emma"]
# heights = [180,165,170]
names = ["Alice","Bob","Bob"]
heights = [155,185,150]

print(sortPeople(names, heights))