## This is the same project of student_sunction.py using Classes:

class student:
    def __init__(self, name, age, grade, sub_list):
        self.name = name
        self.age = age
        self.grade = grade
        self.sub_list = sub_list

    def print_student_details(self):
        print("{}, {}, {}".format(self.name, self.age, self.grade, self.sub_list))

    def give_exam(self):
        print(self.name + " is giving an exam")


tom = student("Tom", 10, 5, ["Math", "Science"])
Jill = student("Jill", 9, 4, ["Language", "History"])
lilly = student("lilly", 9, 4, ["Language", "History"])

tom.print_student_details()
Jill.print_student_details()
lilly.print_student_details()


















