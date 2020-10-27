from typing import List

def csWhereIsBob(names: List[str]) -> int:
    #list of names
    #create variable to store value of index
    #iterate through list
    #find first instance where element matches arg
    #return index where 'Bob' exists
    #if none, return -1
    for name in names:
      if name == 'Bob':
        return names.index(name)

    return -1

# Could also use for i in range(len(names)): to iterate through indices
print(csWhereIsBob(["Jimmy", "Layla", "Bob"]))
print(csWhereIsBob(["Jimmy", "Layla"]))


# function csWhereIsBob(arr) {
#   for (let i = 0; i < arr.length; i++) {
#     if (arr[i] === 'Bob') {
#       return i;
#       } 
#     }
#    return - 1
#  }