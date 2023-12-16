def digit_count(num):
    for index ,i in enumerate(num):
        if num.count(str(index)) != int(i):
            return False
    return True

print(digit_count("030"))