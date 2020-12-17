def csSchoolYearsAndGroups(years: int, groups: int) -> str:
    #set empty string to add on to
    #loop through years and groups
    letters = 'abcdefghijklmnopqrstuvwxyz'
    years_groups = ''
    for year in range(years):
        for char in range(groups):
            years_groups += f"{year + 1}{letters[char]}, "
    return years_groups[0:len(years_groups) - 2]

print(csSchoolYearsAndGroups(3,3))