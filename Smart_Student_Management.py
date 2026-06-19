class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, marks, standard):
        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100")
        super().__init__(name, age)
        self.marks = marks
        self.standard = standard

    def display_info(self):
        super().display_info()
        print(f"Standard: {self.standard}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.get_grade()}\n")

    def get_grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 75:
            return 'B'
        elif self.marks >= 50:
            return 'C'
        else:
            return 'F'

    def is_pass(self):
        return self.marks >= 50


class Teacher(Person):
    def __init__(self, name, age, subject, experience):
        super().__init__(name, age)
        self.subject = subject
        self.experience = experience

    def display_info(self):
        super().display_info()
        print(f"Subject: {self.subject}")
        print(f"Years of Experience: {self.experience}")

    def is_senior(self):
        return self.experience >= 5


student_list = []
teacher_list = []


def add_student():
    try:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        marks = float(input("Enter marks: "))
        standard = input("Enter standard: ")

        if age <= 0:
            raise ValueError("Age must be a positive number.")
        student = Student(name, age, marks, standard)
        student_list.append(student)
        print(f"{name} has been successfully  added.")

    except ValueError as e:
        print(f"Error: {e}")


def view_student():
    if not student_list:
        print("No students found. Please add student first.")
        return

    print(f"Total Students: {len(student_list)}")
    print("=" * 40)
    for i, student in enumerate(student_list, 1):
        print(f"Student: {i}")
        student.display_info()
        print("=" * 40)


def search_student():
    if not student_list:
        print("No students found. Please add student first.")
        return
    search_name = input("Enter name to search: ")

    found = False
    for student in student_list:
        if student.name.lower() == search_name.lower():
            student.display_info()
            found = True

    if not found:
        print("Student not found.")


def update_marks():
    if not student_list:
        print("No students found. Please add student first.")
        return

    student_name = input("Enter the name of student: ")

    if not student_name.strip():
        print("Name cannot be empty.")
        return
    try:
        marks = float(input("Enter new marks: "))
        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 to 100.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    found = False
    for student in student_list:
        if student.name.lower() == student_name.lower():
            student.marks = marks
            print(f"{student.name}'s marks updated to {marks}")
            found = True
            break

    if not found:
        print("Student not found.")


def delete_student():
    if not student_list:
        print("No students found. Please add student first.")
        return

    student_name = input("Enter the name of student: ")

    if not student_name.strip():
        print("Name cannot be empty.")
        return

    found = False
    for student in student_list:
        if student.name.lower() == student_name.lower():
            student_list.remove(student)
            print(f"{student.name} has been deleted successfully.")
            found = True
            break

    if not found:
        print("Student not found.")


def add_teacher():
    try:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        subject = input("Enter subject: ")
        experience = int(input("Enter years of experience: "))

        if age <= 0:
            raise ValueError("Age must be a positive number.")
        if experience < 0:
            raise ValueError("Experience cannot be negative.")
        teacher = Teacher(name, age, subject, experience)
        teacher_list.append(teacher)
        print(f"{name} has been successfully added.")

    except ValueError as e:
        print(f"Error: {e}")


def view_teacher():
    if not teacher_list:
        print("No teachers found. Please add teacher first.")
        return

    print(f"Total Teachers: {len(teacher_list)}")
    print("=" * 40)
    for i, teacher in enumerate(teacher_list, 1):
        print(f"Teacher: {i}")
        teacher.display_info()
        print("=" * 40)


def get_average():
    if not student_list:
        print("No students found. Please add student first.")
        return

    total = sum(student.marks for student in student_list)
    average = total / len(student_list)
    print(f"Average: {average: .2f}")


def get_highest():
    if not student_list:
        print("No students found. Please add student first.")
        return

    top = max(student_list, key=lambda s: s.marks)
    print(f"Highest Scorer: {top.name} with {top.marks} marks.")


def get_lowest():
    if not student_list:
        print("No students found. Please add student first.")
        return

    bottom = min(student_list, key=lambda s: s.marks)
    print(f"Lowest Scorer: {bottom.name} with {bottom.marks} marks.")


def pass_fail_count():
    if not student_list:
        print("No students found. Please add student first.")
        return

    pass_count = 0
    fail_count = 0
    for student in student_list:
        if student.is_pass():
            pass_count += 1

        else:
            fail_count += 1

    print(f"The count for the pass student: {pass_count}")
    print(f"The count for the fail student: {fail_count}")


def save_data():
    if not student_list:
        print("No students found. Please add student first.")
        return
    try:
        with open("students.txt", "w") as f:
            for student in student_list:
                f.write(
                    f"{student.name},{student.age},{student.marks},{student.standard}\n")
            print("Data saved successfully.")
    except Exception as e:
        print(f"Error saving data: {e}")


def load_data():
    try:
        with open("students.txt", "r") as f:
            student_list.clear()
            for line in f:
                name, age, marks, standard = line.strip().split(",")
                student = Student(name, int(age), float(marks), standard)
                student_list.append(student)
            print("Data loaded successfully.")
    except FileNotFoundError as e:
        print(f"No data found. Please save data first.")


def main_menu():
    while True:
        print("=" * 40)
        print("SMART STUDENT MANAGEMENT SYSTEM")
        print("=" * 40)
        print("---Student Management----")
        print("1. Add student")
        print("2. View student")
        print("3. Search student")
        print("4. Update student")
        print("5. Delete student")
        print("---Teacher Management----")
        print("6. Add teacher")
        print("7. View teacher")
        print("---Analytics----")
        print("8. Average Marks")
        print("9. Highest Scorer")
        print("10. Lowest Scorer")
        print("11. Pass / Fail Count")
        print("---File Handling----")
        print("12. Save Data")
        print("13. Load Data")
        print("14. Exit")
        print("=" * 40)

        choice = input("Enter your choices (1-14): ")
        if choice == '1':
            add_student()
        elif choice == '2':
            view_student()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_marks()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            add_teacher()
        elif choice == '7':
            view_teacher()
        elif choice == '8':
            get_average()
        elif choice == '9':
            get_highest()
        elif choice == '10':
            get_lowest()
        elif choice == '11':
            pass_fail_count()
        elif choice == '12':
            save_data()
        elif choice == '13':
            load_data()
        elif choice == '14':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter between 1 to 14.")


main_menu()
