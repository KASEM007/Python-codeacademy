from Mk import Employee
from Internship import Student


employee_1 = Employee("Huda Kasem", "Sales", 25, 60000, True)
employee_2 = Employee("Doaa Kasem", "Sales", 25, 80000, True)
employee_3 = Employee("Susu Hany", "Sales", 25, 70000, False)
employee_4 = Employee("Nikki Salehje", "HR", 25, 90000, True)
employee_5 = Employee("Tylor Swift", "securtary", 25, 40000, False)

student_1 = Student("Mahmud", "Ahmed", 3.5, "Engineer", "Asuit University")
student_2 = Student("Alla", "Galal", 3.2, "low", "Asuit University")
student_3 = Student("Nagla", "Kasem", 3.9, "History", "Cairo University")
student_4 = Student("Hany", "Salah", 3.6, "Social Work", "Helwan University")

print(student_3.first_name, student_3.last_name)
