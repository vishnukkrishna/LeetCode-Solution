# 2418. Sort the People

def sort_names(names,heights):

    n=len(heights)

    for i in range(n-1):
        for j in range(n-i-1):
            if heights[j]<heights[j+1]:
                heights[j],heights[j+1]=heights[j+1],heights[j]
                names[j],names[j+1]=names[j+1],names[j]
    return names

names=['john','crestapher','karthi' ]
heights=[120,82,190]
l=sort_names(names,heights )
print('The sorted names in terms of heights',l)