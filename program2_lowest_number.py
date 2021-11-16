#  Program 2
#  Create a program that ask 3 numbers.
#  Find the lowest number using only if-else statement.
#  Display the lowest number

def get_input():
    print("Hi,\n\n")
    first_i = int(input("Please enter the 1st number: "))
    second_i = int(input("Please enter the 2nd number: "))
    third_i = int(input("Please enter the 3rd number: "))
    return first_i, second_i, third_i


def min_of_three(first_no, second_no, third_no):
    if (first_no < second_no and first_no < third_no) or (first_no == second_no < third_no) or (first_no == third_no < second_no) or (first_no == second_no == third_no):
        return first_no
    elif (second_no < first_no and second_no < third_no) or (second_no == first_no < third_no) or (second_no == third_no < first_no):
        return second_no
    elif (third_no < first_no and third_no < second_no) or (third_no == first_no < second_no) or (third_no == second_no < first_no):
        return third_no

first, second, third = get_input()
min = min_of_three(first, second, third)
print(f"\nLowest number: {min}\n")