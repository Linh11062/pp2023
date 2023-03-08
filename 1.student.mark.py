students = {}
courses = {}
marks = {}

def input_students():
    num_students = int(input("Enter number of students in the class: "))
    for i in range(num_students):
        print(f"---Student No.{i+1}---")
        students[input("id of student: ")] = {"name": input("name of student: "), "dob": input("birthday: ")}    

def input_courses():
    num_courses = int(input("Enter number of courses: "))
    for j in range(num_courses):
        print(f"---Course No.{j+1}---")
        courses[input("id of course: ")] = {"name" : input("name of course: ")}

def input_marks():
    id_student = input("Select id_student to enter mark: ")
    id_course = input("Select id_sourse to enter mark: ")
    for id_student in students:
        mark = float(input(f"Enter mark for {students[id_student]['name']}"))
        if id_student not in marks:
            marks[id_student] = {}
        marks[id_student][id_course] = mark

def list_courses():
    id_course = input("Select id_sourse: ")
    for id_course in courses:
        print(f"{id_course}: {courses[id_course]['name']}")

def list_students():
    id_student = input("Select id_student: ")
    for student_id in students:
        print(f"{id_student}: {students[id_student]['name']}")

def show_marks():
    course_id = input("Show mark of course ID: ")
    if course_id not in courses:
        print("Invalid course ID")
        return
    else:
        for student_id in students:
            print(f"{students[student_id]['name']}: {marks[student_id][course_id]}")

def main():
    input_students()
    input_courses()
    input_marks()
    list_courses()
    list_students()
    show_marks()
main()