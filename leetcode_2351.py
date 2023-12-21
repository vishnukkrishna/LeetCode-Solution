def repeatedCharacter(s):
    container = set()

    for value in s:
        if value in container:
            return value
        else:
            container.add(value)
        
string = 'jkodgypoya'
print(repeatedCharacter(string))