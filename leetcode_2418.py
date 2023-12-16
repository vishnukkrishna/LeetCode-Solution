
def sort_people(names, heights):
    ziped_array = zip(heights ,names)
    arr = dict(ziped_array)
    sorted_dict = {key: value for key, value in sorted(arr.items(), key= lambda item: item[0], reverse=True)}
    return list(sorted_dict.values())
    
    # short hand method
    # sorted_people = [name for _, name in sorted(zip(heights, names), key=lambda x: x[0], reverse=True)]
    # return sorted_people


names = ['Mary', 'John', 'Emma']
heights = [180, 165, 170]
print(sort_people(names, heights))