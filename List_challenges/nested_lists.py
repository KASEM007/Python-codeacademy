# Nested_lists
# Given the names and grades for each student in a Physics class of  students,
# store them in a nested list and print the name(s) of any student(s) having
# the second lowest grade.

# Note: If there are multiple students with the same grade, order their names
# alphabetically and print each name on a new line.

# Explanation 0
# There are  students in this class whose names and grades are assembled to build
# the following list:

# python students = [
# ['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]
# ]

# The lowest grade of  belongs to Tina.
# The second lowest grade of  belongs to both Harry and Berry, so we order their
# names alphabetically and print each name on a new line.

    dic = {}
    s = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in dic:
            dic[score].append(name)
        else:
            dic[score] = [name]
        if score not in s:
            s.append(score)
        m = min(s)
    s.remove(m)
    m1 = min(s)
    dic[m1].sort()
    for i in dic[m1]:
        print(i)
