#  Program 2
#  Create a program that ask 3 numbers.
#  Find the lowest number using only if-else statement.
#  Display the lowest number

def get_input():    # function to collect inputs
    print("Hi,\n\n")
    first_i = input("Please enter the 1st number: ")
    second_i = input("Please enter the 2nd number: ")
    third_i = input("Please enter the 3rd number: ")
    return first_i, second_i, third_i


def input_validation(first_try, second_try, third_try):
    if (first_try != "") and (second_try != "") and (third_try != ""): # if inputs are not empty, the program continues
        try:
            first_int, second_int, third_int = float(   # converts inputs into float datatype to enable inputs with decimal points
                first_try), float(second_try), float(third_try)
            if (first_int - int(first_int) == 0):   # if the input is a whole number, it will be converted into int datatype to flash the original input back if it is the lowest
                first_int = int(first_int)          # for example, without these codes, an input of 1 will be flashed as 1.0. But with this, input 1 will be flashed as 1

            if (second_int - int(second_int) == 0):
                second_int = int(second_int)

            if (third_int - int(third_int) == 0):
                third_int = int(third_int)

            return first_int, second_int, third_int

        except ValueError:
            print("\nError. Please enter numbers.") # inputs that can't be converted to float datatype is restricted
            return False, False, False
    else:
        print("\nEmpty input is invalid. Please try again.")    # restricts empty inputs
        return False, False, False
    # This time, negative inputs are allowed

def min_of_three(first_no, second_no, third_no):    # conditions to classify the input or inputs (if two or three inputs are equal) with the lowest value
    if (first_no < second_no and first_no < third_no) or (first_no == second_no < third_no) or (first_no == third_no < second_no) or (first_no == second_no == third_no):
        return first_no
    elif (second_no < first_no and second_no < third_no) or (second_no == first_no < third_no) or (second_no == third_no < first_no):
        return second_no
    elif (third_no < first_no and third_no < second_no) or (third_no == first_no < second_no) or (third_no == second_no < first_no):
        return third_no


first, second, third = get_input() # storing inputs in different variables
first_valid, second_valid, third_valid = input_validation(first, second, third)
if (first_valid != False) and (second_valid != False) and (third_valid != False):   # if the input_validation() function did not return a false value, the program proceeds
    min = min_of_three(first_valid, second_valid, third_valid)
    print(f"\nLowest number: {min}\n")
