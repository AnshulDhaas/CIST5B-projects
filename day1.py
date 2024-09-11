def writeVertical(n):
    if n < 10:
        print(f"{n}")
    else:
        writeVertical(n // 10)
        print(f"{n % 10}")
        
def writeVerticalNeg(n):
    if n < 0:
        print("-")
        n = -n 

    if n < 10:
        print(f"{n}")
    else:
        writeVerticalNeg(n // 10)
        print(f"{n % 10}")

        