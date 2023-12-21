def percentage_letter(s, letter):
    val = (letter.count(s)) 
    return round((val/len(letter)) * 100)


letter = "foobar"
key = "o"

print(percentage_letter(key, letter))