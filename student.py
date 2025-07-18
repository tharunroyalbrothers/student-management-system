import os
import csv

EXCEL_FILE = "students.csv"

def init_excel():
    if not os.path.exists(EXCEL_FILE):
        with open(EXCEL_FILE,"w",newline="") as f:
            writer=csv.writer(f)
            writer.writerow(["Roll No","Name","Age","Course","Email"])

class Student():
    def __init__(self,roll_no,name,age,course,email):
        self.roll_no = roll_no.upper()
        self.name = name.title()
        self.age = age
        self.course = course.title()
        self.email = email.lower()
    def __str__(self):
        return f"Roll No: {self.roll_no}, Name: {self.name}, Age: {self.age}, Course: {self.course} , Email: {self.email}"

students={}

course_map={
    "cse":"compter science",
    "cs":"compter science",
    "computer science":"compter science",
    "ise":"information science",
    "it":"information science",
    "information science":"information science",
    "ece":"electronics and communication",
    "ec":"electronics and communication",
    "electronics and communication":"electronics and communication",
    "civil":"civil engineering",
    "cv":"civil engineering",
    "civil engineering":"civil engineering",
    "me":"mechanical engineering",
    "mech":"mechanical engineering",
    "mec":"mechanical engineering",
    "mechanical engineering":"mechanical engineering",
    "ae":"aeronautical engineering",
    "aero":"aeronautical engineering",
    "aeronautical engineering":"aeronautical engineering",
    "aiml":"artificial intelligence and machine learning",
    "ai":"artificial intelligence and machine learning",
    "artificial intelligence and machine learning":"artificial intelligence and machine learning",
    "csd":"computer science and design",
    "computer science and design":"computer science and design",
    }

def get_name():
    name = ' '.join(input("Enter your Name: ").strip().split())
    if not name:
        raise ValueError("Name can't be empty")
    elif name.isdigit():
        raise ValueError("Name can't be a number")
    elif '..' in name:
        raise ValueError("Name is invalid")
    elif name.endswith('.'):
        raise ValueError("Name is invalid")
    elif name.startswith('.'):
        raise ValueError("Name is invalid")
    elif not all(char.isalpha() or char.isspace() or char == '.' for char in name):
        raise ValueError("Name is Invalid")
    return name

def get_age():
    age_input=input("Enter your Age:").strip()
    if not age_input.isdigit():
        raise ValueError("Age is Invalid")
    age=int(age_input)
    if age<=0 or age>=100:
        raise ValueError("Age is Invalid")
    return age

def get_course():
    course_input = input("Enter your Course: ").strip().lower()
    if not course_input:
        raise ValueError("Course can't be empty")
    elif not all(char.isalpha() or char.isspace() for char in course_input):
        raise ValueError("Invalid Course")
    elif course_input not in course_map:
        raise ValueError("Course not recognized.")
    return course_map[course_input]


def get_roll_no():
    roll_no = input("Enter the Roll No: ").strip().upper()    
    if len(roll_no) != 10:
        raise ValueError("Invalid Roll No")
    elif roll_no[0] != '1' or roll_no[1:3].lower() != 'sj':
        raise ValueError("Invalid Roll No")
    elif not roll_no[5].isalpha() or not roll_no[6].isalpha():
        raise ValueError("Invalid Roll No")
    for pos in [3, 4, 7, 8, 9]:
        if not roll_no[pos].isdigit():     
            raise ValueError("Invalid Roll No")
    return roll_no

def get_email():
    email_input = input("Enter the Email:").strip()
    if not email_input:
        raise ValueError("Email can't be empty")
    elif any(s.email == email_input.lower() for s in students.values()):
        raise ValueError("Email already exists")
    elif '..' in email_input:
        raise ValueError("Invalid Email")
    elif email_input.startswith('.'):
        raise ValueError("Invalid Email")
    elif email_input.endswith('.'):
        raise ValueError("Invalid Email")
    elif email_input.startswith('-'):
        raise ValueError("Invalid Email")
    elif email_input.endswith('-'):
        raise ValueError("Invalid Email")
    elif '..' in email_input:
        raise ValueError("Invalid Email")
    elif '--' in email_input:
        raise ValueError("Invalid Email")
    elif '.-' in email_input:
        raise ValueError("Invalid Email")
    elif '-.' in email_input:
        raise ValueError("Invalid Email")
    elif ' ' in email_input:
        raise ValueError("Invalid Email")
    elif email_input.count('@') !=1:
        raise ValueError("Invalid Email")
    return email_input

def add_student():
    try:
        roll_no=get_roll_no()
        if roll_no in students:
            print("Roll number already exists")
            return
        name = get_name()
        age = get_age()
        course = get_course()
        email = get_email()
        
        student=Student(roll_no,name,age,course,email)
        students[roll_no] = student   #you are storing the object student in the dictionary with roll_no as the key.
        
        print("\nStudent details added successfully")
        save_student_to_csv(student)

        
    except ValueError as e:
        print(f"Error: {e}")     
        
def save_student_to_csv(student):
    file_exists=os.path.exists(EXCEL_FILE)
    with open(EXCEL_FILE,"a",newline="") as f:
        writer= csv.writer(f)
        if os.path.getsize(EXCEL_FILE)==0:
            writer.writerow(["Roll No","Name","Age","Course","Email"])  
        writer.writerow([student.roll_no,student.name,student.age,student.course,student.email])

def load_students_from_csv():
    if os.path.exists(EXCEL_FILE):
        with open(EXCEL_FILE,"r",newline="") as f:
            reader=csv.DictReader(f)
            for row in reader:
                try:
                    roll_no = str(row["Roll No"]).strip().upper()
                    name = str(row["Name"]).strip().title()
                    age = int(row["Age"])
                    email= str(row["Email"]).strip()
                    course_raw = str(row["Course"]).strip().lower()
                    course = course_map.get(course_raw, course_raw)
                    students[roll_no] = Student(roll_no, name, age, course, email)
                except Exception:
                    continue  


def write_all_students_to_csv():
    with open(EXCEL_FILE,"w",newline="") as f:
        writer= csv.writer(f)
        writer.writerow(["Roll No","Name","Age","Course","Email"])
        for student in students.values():
            writer.writerow([student.roll_no,student.name,student.age,student.course,student.email])
        
def view_students():
    if not students:
        print("No students details available")
    else:
        print("\nList of Students:")
        for student in students.values():
            print(student)
            
def update_student():
    roll_no = input("Enter the Roll No of the student to update: ").strip().upper()
    if roll_no not in students:
        print("Student not found.")
        return

    student = students[roll_no]
    print(f"Current details:\n{student}")

    print("\nWhat would you like to update?")
    print("1. Name")
    print("2. Age")
    print("3. Course")
    print("4. Email")
    print("5. Cancel")

    choice = input("Enter your choice (1-5): ").strip()

    try:
        if choice == "1":
            name = get_name()
            student.name = name
        elif choice == "2":
            age=get_age()
            student.age = age
        elif choice == "3":
            course=get_course()
            student.course =course
        elif choice == "4":
            email=get_email()
            student.email =email
        elif choice == "5":
            print("Update cancelled.")
            return
        else:
            print("Invalid choice.")
            return

        print("Student details updated successfully.")
        write_all_students_to_csv()

    except ValueError as e:
        print(f"Error: {e}")
        
        
def delete_student():
    roll_no = input("Enter the Roll No of the student to delete: ").strip().upper()
    
    if roll_no not in students:
        print("Student not found.")
        return

    student = students[roll_no]
    print("\nStudent details:")
    print(student)  

    confirm = input("\nAre you sure you want to delete this student? (yes/no): ").strip().lower()
    if confirm == "yes":
        del students[roll_no]
        print("Student deleted successfully.")
        write_all_students_to_csv()

    else:
        print("Deletion cancelled.")



if __name__ == "__main__":
    init_excel()
    load_students_from_csv()
    while True:
        print("\n=== Student Management System ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Details")
        print("4. Delete Student details")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Thank you")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, 3, 4 or 5.")