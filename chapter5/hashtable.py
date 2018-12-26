voted = {}


def check_voter(name):
    if voted.get(name):
        print("Kick {0} out".format(name))
    else:
        voted[name] = True
        print("{0} has voted".format(name))


check_voter("mike")
check_voter("jane")
check_voter("mike")

book = dict()
book["Golang"] = 1800
book["Python"] = 1200
book["Scala"] = 1500
book["Java"] = 500
for key in book.keys():
    print("{0} is {1} yen.".format(key, book[key]))


