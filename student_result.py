# Student Result Management System
# Internship Project
# Developed using Python
# Author: Shivani Mandlik

# Dictionary to store student records
students = {}

# Function to calculate grade based on percentage
def calculate_grade(percentage):
    if percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 40:
        return "C"
    else:
        return "Fail"

# Function to add a new student record
def add_student():
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Student Name: ")

    marks = []
    for i in range(3):
        mark = int(input(f"Enter marks for Subject {i+1}: "))
        marks.append(mark)

    total = sum(marks)
    percentage = total / len(marks)
    grade = calculate_grade(percentage)

    students[roll] = {
        "name": name,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade
    }

    print("\nStudent record added successfully!\n")

# Function to view student result
def view_student():
    roll = int(input("Enter Roll Number to view result: "))

    if roll in students:
        s = students[roll]
        print("\n--- Student Result ---")
        print("Name       :", s["name"])
        print("Marks      :", s["marks"])
        print("Total Marks:", s["total"])
        print("Percentage :", s["percentage"])
        print("Grade      :", s["grade"])
        print("----------------------\n")
    else:
        print("\nStudent record not found!\n")

# Main menu-driven program
while True:
    print("===== Student Result Management System =====")
    print("1. Add Student")
    print("2. View Student Result")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_student()
    elif choice == "3":
        print("Thank you for using the system!")
        break
    else:
        print("Invalid choice! Please try again.\n")
