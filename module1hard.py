grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
student_sorted_list = sorted(list(students))
grades_mark = []
ccc = 0
for i in grades:
    ccc = sum(i) / len(i)
    grades_mark.append(ccc)
students_dict = dict(zip(student_sorted_list, grades_mark))
print(students_dict)
