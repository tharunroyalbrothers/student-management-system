# Student Management System

A simple **Student Management System** allows user to add,view,update and delete the students details in a college. This project is ideal for learning the basics of CRUD operations, data storage, and simple user interface design.

## Features

--> Add new students details such as roll number(e.i university seat number), name of the student,
age of the student and course of the student(i.e branch).
--> View the list of all students details added.
--> Update the students details if required (name,age,course).
--> Delete the student details if required.

## How to Run

--> Ensure you have **Python 3.x** installed on your system.
--> Download or clone this repository.
--> Navigate to the project directory in the terminal.
--> Run the script.


## Features
 
--> Add new student with validations.
--> View all students details.
--> update student information (Nmae,Age,Course)
--> Delete student details.
--> Course name normalization (e.g 'cse','cs',and 'computer science'all map to 'Computer Science')

## Role number format

--> Here it must contain 10characters
--> Format example: 1SJ21CS001
--> Validations
    1. It should start with '1SJ' only if it error is raised.
    2. It has 2 letters at position 5 and 6 which represents the course.
    3. Integers are specified to 7,8 and 9 position only.

## Name format

--> Name cant be empty or can not contain special characters.
--> Accepts alphabetics and periods(.)
--> Before and after every period(.) there must be an alphabetic.

## Age format

--> Age must be positive interger always.
--> Age is constrained from 1 to 99 only here.

## Course format

--> Accepts full names and common abbrivations(e.g cse,ec,mech,etc.)
--> Internally maps to standard course name.

## Code Organization

--> Student Class for representing student objects.
--> Modular input functions:
    1. get_name()
    2. get_age()
    3. get_course()
--> Main operations:
    1. add_student()
    2. view_students()
    3. update_student()
    4. delete_student()
--> Menu driven loop under if __name__=="__main__":