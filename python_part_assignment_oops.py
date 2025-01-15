# Question 1
"""Build a program to manage a university's course catalog.You want to define a base class Course that has the following properties:
course_code: a string representing the course code (e.g., "CS101")
course_name: a string representing the course name (e.g., "Introduction to Computer Science")
credit_hours: an integer representing the credit hours for the course (e.g., 3)
You also want to define two subclasses CoreCourse and ElectiveCourse, which inherit from the Course class.
CoreCourse should have an additional property required_for_major which is a boolean representing whether the course is required for
a particular major. ElectiveCourse should have an additional property elective_type which is a string representing the type of elective """


class Course:
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours

    def display_course_info(self):
        print(f"Course Code: {self.course_code}")
        print(f"Course Name: {self.course_name}")
        print(f"Credit Hours: {self.credit_hours}")


class CoreCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, required_for_major):
        super().__init__(course_code, course_name, credit_hours)
        self.required_for_major = required_for_major

    def display_course_info(self):
        super().display_course_info()
        print(f"Required for Major: {'Yes' if self.required_for_major else 'No'}")


class ElectiveCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, elective_type):
        super().__init__(course_code, course_name, credit_hours)
        self.elective_type = elective_type

    def display_course_info(self):
        super().display_course_info()
        print(f"Elective Type: {self.elective_type}")



core_course = CoreCourse("CS101", "Introduction to Computer Science", 3, True)
print("Core Course:")
core_course.display_course_info()

print("\nElective Course:")
elective_course = ElectiveCourse("HIST210", "World History", 3, "liberal arts")
elective_course.display_course_info()

# Question2:

""" Create a Python module named employee that contains a class Employee with attributes name, salary and methods get_name() and get_salary().
Write a program to use this module to create an object of the Employee class and display its name and salary."""


from employee import Employee

# Create an object of the Employee class
employee1 = Employee("ANU", 50000)

# Display the name and salary of the employee
print(f"Employee Name: {employee1.get_name()}")
print(f"Employee Salary: ${employee1.get_salary()}")

