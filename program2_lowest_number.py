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


first, second, third = get_input()