"""     2678. Number of Senior Citizens    """


def countSeniors(data):
    arr = [i.isdigit()[10:12] for i in data]
    print(arr)


details = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
print(countSeniors(details))
