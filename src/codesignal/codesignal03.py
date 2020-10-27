def csOppositeReverse(txt: str) -> str:
    #input is only alpha characters
    #return string in reverse order with opposite casing
    return txt.swapcase()[::-1]

print(csOppositeReverse("Hello World"));