def largest_good_integer(num):
    for i in range(9, -1, -1):
        if str(i) + str(i) + str(i) in num:
            return str(i) + str(i) + str(i)
    return ""


num = "12344456888"

print(largest_good_integer(num))