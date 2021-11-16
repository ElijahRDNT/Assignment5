#  Program 2
#  Create a program that ask 3 numbers.
#  Find the lowest number using only if-else statement.
#  Display the lowest number

def get_input():
    print("Hi,\n\n")
    first_i = input("Please enter the 1st number: ")
    second_i = input("Please enter the 2nd number: ")
    third_i = input("Please enter the 3rd number: ")
    return first_i, second_i, third_i


def input_validation(first_try, second_try, third_try):
    if (first_try != "") and (second_try != "") and (third_try != ""):
        try:
            first_int, second_int, third_int = float(
                first_try), float(second_try), float(third_try)

            return first_int, second_int, third_int

        except ValueError:
            print("\nError. Please enter numbers.")
            return False, False, False
    else:
        print("\nEmpty input is invalid. Please try again.")
        return False, False, False


def min_of_three(first_no, second_no, third_no):
    if (first_no < second_no and first_no < third_no) or (first_no == second_no < third_no) or (first_no == third_no < second_no) or (first_no == second_no == third_no):
        return first_no
    elif (second_no < first_no and second_no < third_no) or (second_no == first_no < third_no) or (second_no == third_no < first_no):
        return second_no
    elif (third_no < first_no and third_no < second_no) or (third_no == first_no < second_no) or (third_no == second_no < first_no):
        return third_no

first, second, third = get_input()
first_valid, second_valid, third_valid = input_validation(first, second, third)
if (first_valid != False) and (second_valid != False) and (third_valid != False):
    min = min_of_three(first_valid, second_valid, third_valid)
    print(f"\nLowest number: {min}\n")