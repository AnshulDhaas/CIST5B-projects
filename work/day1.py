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

def writeVerticalIter(n):
    if n<0:
        print("-")
        n = -n
    arr=[]
    while n >= 10:
        arr.append(n % 10)
        n = n // 10
    
    for num in reversed(arr):
        print(num)

def even(listOfOnes, index):
    if index == len(listOfOnes):
        return "Even"
    if listOfOnes[index] == 1:
        return odd(listOfOnes, index+1)
    else:
        return even(listOfOnes, index+1)
    
def odd(listOfOnes, index):
    if index == len(listOfOnes):
        return "Odd"
    if listOfOnes[index] == 1:
        return even(listOfOnes, index+1)
    else:  
        return odd(listOfOnes, index+1)