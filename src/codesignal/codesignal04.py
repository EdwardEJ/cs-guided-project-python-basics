def csSquareAllDigits(n: int) -> int:
    #split n into individual integers
    #square each integer
    #join numbers
    #return joined numbers
    
    # newArr = []
    # splitN = [int(i) for i in str(n)]
    # for val in splitN:
    #   newArr.append((val)** 2)

    # return int("".join("{0}".format(n) for n in newArr))

    return int(''.join(str(int(i)**2) for i in str(n)))

print(csSquareAllDigits(9119))