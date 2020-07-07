## Here will have the same program using just functions and then using classes:

dict_student = {} # key(student name) : value list [age, grade, [list of subject]

def add_student(name):
    dict_students[name] = []
    return dict_students

def add_student_details(student, age, grade, sub_list = None):
    if sub_list is None:
        sub_list = []
    dict_students[student] = [age, grade, sub_list]

def remove_student(student):
    if student in dict_students:
        dict_students.pop(student)

def print_student_details(name):
    print("{}, {}, {}.format(name, dict_students[name][0], dict_students[name][1], dict_students[name][2])")
    #print(f"Name: {dict_students[name][0]}, {dict_students[name][1]}, {dict_students[name][2]}")


def exam(name):
    print(name + " is giving an exam")

add_student("Tom")
add_student_details("Tom", 10, 5, ['Math', 'Science'])
add_student("Jill")
add_student_details("Jill", 9, 4, ['Geography', 'History'])

print_student_details("Tom")
print_student_details("Jill")
exam("Tom")
exam("Teacher")





































        
        
        
