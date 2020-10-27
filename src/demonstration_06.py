"""
Challenge #6:

Create a function that takes a string, checks if it has the same number of "x"s
and "o"s and returns either True or False.

- Return a boolean value (True or False).
- The string can contain any character.
- When no x and no o are in the string, return True.

Examples:
- XO("ooxx") ➞ True
- XO("xooxx") ➞ False
- XO("ooxXm") ➞ True (Case insensitive)
- XO("zpzpzpp") ➞ True (Returns True if no x and o)
- XO("zzoo") ➞ False
"""
def XO(txt: str) -> bool:
    # Your code here
    # how do we keep track of the number of "x"s and "o"s
    # let's keep two variables for each
    # figure out the number of "o"s and "x"s in the input string
    # look at each character and iterate through the `txt` string
      # if o, increment xs
      # if x, increment os
    # check if they are the same amount
    # return True if they are, False otherwise

    # accommodate for case insensitivity
    xs = 0
    os = 0
    for character in txt:
      if character.lower() == "x":
        xs += 1
      if character.lower() == "o":
        os += 1

    # if xs == os:
    #   return True
    # else:
    #   return False

    return xs == os

print(XO("ooxx"))
print(XO("xooxx"))
print(XO("ooxXm"))
print(XO("zpzpzpp"))