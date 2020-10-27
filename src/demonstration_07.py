"""
Challenge #7:

Given an unsorted list, create a function that returns the nth smallest element
(the smallest element is the first smallest, the second smallest element is the
second smallest, etc).

Examples:
- nth_smallest([7, 5, 3, 1], 1) ➞ 1
- nth_smallest([1, 3, 5, 7], 3) ➞ 5
- nth_smallest([1, 3, 5, 7], 5) ➞ None
- nth_smallest([7, 3, 5, 1], 2) ➞ 3
"""
from typing import List

def nth_smallest(lst: List[int], n: int) -> int:
    # Your code here
    # given unsorted array, find nth smallest
    # note that smallest element is the first smallest
    # how can we find the nth smallest
    # return nth smallest number
    if n > len(lst):
      return None
    lst.sort()
    nth_smallest = lst[n - 1]
    return nth_smallest
  
print(nth_smallest([1, 3, 5, 7], 3))
print(nth_smallest([1, 3, 5, 7], 5))
