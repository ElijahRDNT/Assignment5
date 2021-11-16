# Program 1: PUP Grading System
# Section 8 of https://www.pup.edu.ph/studentservices/files/ThePUPStudentHandbook2014.pdf
# Create a program that will ask for grade percentage. Display the equivalent Grade/Mark and Description
# Example:
# Input grade: 87.6
# Grade/Mark: 1.75
# Description: Very Good

def get_input():
    print("\nGood day!")
    grade_input = input(
        "\nNote: Avoid putting unnecessary symbols. Only numbers and a decimal point(if applicable) are allowed. Thank you.\n\nInput grade: ")
    return grade_input

grade = get_input()