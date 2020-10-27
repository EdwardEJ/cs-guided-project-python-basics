"""
Challenge #2:

Write a function that takes an integer `minutes` and converts it to seconds.

Examples:
- convert(5) ➞ 300
- convert(3) ➞ 180
- convert(2) ➞ 120
"""
def convert(minutes: int) -> int:
    # Your code here
    # 60 seconds in a minute
    # need to take `minutes` and multiply by 60
    # in order to perform conversion
    # return converted result
    seconds = minutes * 60
    return seconds
    #return str(seconds)

print(convert(5))
## Typescript
'''
function convert (minutes: number): number {
    const seconds = minutes * 60;
    return seconds;
}
'''