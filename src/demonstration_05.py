"""
Challenge #5:

Create a function that returns a list of strings sorted by length in ascending
order.

Examples:
- sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
- sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]
- sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]
- sort_by_length([]) ➞ []
"""
def sort_by_length(lst):
    # Your code here
    # takes a list of strings and sorts them in such a way that
    # the shorter strings comes first with the longest string last
    # how do we sort an array/list by the length of the elements?
    # the `.sort` method on lists in Python sorts in-place
    # the `.sort` method defaults to sorting strings in alphabetical order
    # we need to tell the sort method that we want to sort by the length
    # use key parameter on the `.sort` method
    # return sorted output 
    lst.sort(key=len)
    return lst

print(sort_by_length(["a", "ccc", "dddd", "bb"]))
print(sort_by_length(["apple", "pie", "shortcake"]))
print(sort_by_length([]))