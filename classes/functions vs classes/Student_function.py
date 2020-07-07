
dict_students = {}   # Key ( Student Name ) : Value list [age, grade, [list of subjects], parent ]
def add_student(name):
    dict_students[name]= []
    return dict_students

def add_student_details(sudent, age, grade, sub_list = None):
    if sub_list is None:
        sub_list = []
    dict_students[sudent] = [age, grade, sub_list]

def remove_student(student):
    if student in dict_students:
        dict_students.pop(student)

def print_student_details(name):
    print("{},{},{},{}".format(
    name,dict_students[name][0],dict_students[name][1],dict_students[name][2]))

def exam(name):
    print(name +" is giving an exam")

add_student("TOM")
add_student_details("TOM", 10, 5, ["Math","Science"])
add_student("Jill")
add_student_details("Jill", 9, 4, ["Geography","History"])
print_student_details("TOM")
print_student_details("Jill")
exam("TOM")





































        
        
        
