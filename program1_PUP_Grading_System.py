# Program 1: PUP Grading System
# Section 8 of https://www.pup.edu.ph/studentservices/files/ThePUPStudentHandbook2014.pdf
# Create a program that will ask for grade percentage. Display the equivalent Grade/Mark and Description
# Example:
# Input grade: 87.6
# Grade/Mark: 1.75
# Description: Very Good

import math


def get_input():
    print("\nGood day!")
    grade_input = input(
        "\nNote: Avoid putting unnecessary symbols. Only numbers and a decimal point(if applicable) are allowed. Thank you.\n\nInput grade: ")
    return grade_input


def round_half_up(grade_round, decimals=0):
    multiplier = 10 ** decimals
    if (grade_round >= 100.1):
        return 1000
    else:
        rounded_grade = math.floor(grade_round*multiplier + 0.5) / multiplier
        return rounded_grade


def input_validation(grade_try):
    if (grade_try == ""):
        grade_try = "null"
        return grade_try

    else:
        try:
            grade_float = float(grade_try)
            grade_rounded = round_half_up(grade_float)
            return grade_rounded

        except ValueError:
            print(
                "\nInvalid input. Please enter numbers and a decimal point(if applicable) only.\n")
            return False


def grade_classification(grade_classify):
    if (grade_classify == "null"):
        mark = "Blank"
        print(f"Grade/Mark: {mark}")
        return mark

    elif (65 <= grade_classify <= 74):
        mark = 5.0
        print(f"Grade/Mark: {mark}")
        return mark

    elif (grade_classify == 75):
        mark = 3.0
        print(f"Grade/Mark: {mark}")
        return mark

    elif(76 <= grade_classify <= 78):
        mark = 2.75
        print(f"Grade/Mark: {mark}")
        return mark

    elif(79 <= grade_classify <= 81):
        mark = 2.5
        print(f"Grade/Mark: {mark}")
        return mark

    elif(82 <= grade_classify <= 84):
        mark = 2.25
        print(f"Grade/Mark: {mark}")
        return mark

    elif(85 <= grade_classify <= 87):
        mark = 2.0
        print(f"Grade/Mark: {mark}")
        return mark

    elif(88 <= grade_classify <= 90):
        mark = 1.75
        print(f"Grade/Mark: {mark}")
        return mark

    elif(91 <= grade_classify <= 93):
        mark = 1.5
        print(f"Grade/Mark: {mark}")
        return mark

    elif(94 <= grade_classify <= 96):
        mark = 1.25
        print(f"Grade/Mark: {mark}")
        return mark

    elif(97 <= grade_classify <= 100):
        mark = 1.0
        print(f"Grade/Mark: {mark}")
        return mark

    elif(64 >= grade_classify) or (grade_classify == 1000):
        mark = 0
        print("Grade/Mark: Can't be classified")
        return mark


def grade_description(grade_describe):
    if (grade_describe == 1.0) or (grade_describe == 1.25):
        description = "Excellent"
        print(f"Description: {description}\n")

    elif (grade_describe == 1.5) or (grade_describe == 1.75):
        description = "Very Good"
        print(f"Description: {description}\n")

    elif (grade_describe == 2.0) or (grade_describe == 2.25):
        description = "Good"
        print(f"Description: {description}\n")

    elif (grade_describe == 2.5) or (grade_describe == 2.75):
        description = "Satisfactory"
        print(f"Description: {description}\n")

    elif (grade_describe == 3.0):
        description = "Passing"
        print(f"Description: {description}\n")

    elif (grade_describe == 5.0):
        description = "Failure"
        print(f"Description: {description}\n")

    elif (grade_describe == 0):
        description = "Invalid"
        print(f"Description: {description}\n")
        print("\nPlease enter a valid grade (ranging from 64.5 to 100.0).\n")

    elif (grade_describe == "Blank"):
        description = "Incomplete / Withdrawn / Dropped"
        print(f"Description: {description}\n")


grade = get_input()
valid_grade = input_validation(grade)

if (valid_grade != False):
    grade_classified = grade_classification(valid_grade)
    grade_described = grade_description(grade_classified)
