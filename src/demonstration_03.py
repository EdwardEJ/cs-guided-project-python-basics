"""
Challenge #3:

Create a function that takes a string and returns it as an integer.

Examples:
- string_int("6") ➞ 6
- string_int("1000") ➞ 1000
- string_int("12") ➞ 12
"""
def string_int(txt: str) -> int:
    # Your code here
    # check to make sure that `txt` makes sense as an integer
    # `isnumeric` function checks if a string can be represented as a number
    # if true, take string input convert to integer
    # the `int` function does this for you in Python
    # call the `int` function passing it the `txt` input

    # if false, return an error indicating that `txt` is not a number
    # use string interpolation to print out the actual value of `txt`
    # yse f-strings in Python
    if txt.isnumeric() is True:
      converted_int = int(txt)
      return converted_int
    else:
      return f"'{txt}' is not a number"

print(string_int("1000"))
print(string_int("hi"))

# Typescript
'''
function string_int(txt: string) {
    if(Number(txt)) return Number(txt)
    else return `${txt} is not a number`
}
'''