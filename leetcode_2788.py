"   2788. Split Strings by Separator    "

def split_words_by_separator(words, separator):
    result = []
    arr = [i.split(separator) for i in words ]
    
    # return result


words = ["$easy$","$problem$"]
separator = "$"

print(split_words_by_separator(words, separator))