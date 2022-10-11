# pROBLEM_sTATEMENT
# Given the names and grades for each student in a class of  students, 
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# Example

# The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

# alpha
# beta
# Input Format

# The first line contains an integer, , the number of students.
# The  subsequent lines describe each student over  lines.
# - The first line contains a student's name.
# - The second line contains their grade.

# Constraints

# There will always be one or more students having the second lowest grade.
# Output Format

# Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

# Sample Input 0

# 5
# Harry
# 37.22
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# Sample Output 0

# Berry
# Harry
if __name__ == '__main__':
    res = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        res.append([name, score])
    
    temp = [i[1] for i in res]
    temp_set_list = list(set(temp))
    temp_set_list.sort()
    res_filter = list(filter(lambda x : x[1] == temp_set_list[1], res))
    res_filter.sort()
    for i in res_filter:
        print(i[0])