
letters = [
    {"lset1": "A"},
    {"lset1": "AB"},
    {"lset1": "AC"},
    {"lset1": "ABC"},
    {"lset2": "B"},
    {"lset2": "AB"},
    {"lset2": "BC"},
    {"lset2": "ABC"},
    {"lset3": "C"},
    {"lset3": "AC"},
    {"lset3": "BC"},
    {"lset3": "ABC"}
]

def setAlpha():
    letter_set = set()
    for letter in letters:
        if any(value in {"A", "B", "C"} for value in letter.values()):
            letterSet.update(letter.values())
    letterSet = {x for x in letterSet if x in {"A", "B", "C"}}
    print(letter_set)

def setBeta():
    letterSet = set()
    for letter in letters:
        if "AC" in letter.values():
            letterSet.update(letter.values())
    letterSet = {x for x in letterSet if x == "AC"}
    print(letter_set)

def setGamma():
    letterSet = set()
    for letter in letters:
        if any(value in {"AB", "AC", "BC"} for value in letter.values()):
            letterSet.update(letter.values())
    letterSet = {x for x in letterSet if x in {"AB", "AC", "BC"}}
    print(letterSet)

setAlpha()
setBeta()
setGamma()
