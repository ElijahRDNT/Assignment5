# Program 3
# Create a program that ask for an age of a person
# Display the life stage of the person
# 0 - 12 : Kid
# 13 -17 : Teen
# 18 : Debut
# 19 above : Adult

def display_header():       # function for the welcoming header
    print("\nGood day!\n\n")


def get_input():    # function for collecting the input age
    age_input = input("Enter your age to classify your life stage: ")
    return age_input    # returning the value of the input of age from the user


def age_validation(age_try):
    try:
        age_int = int(age_try) # this tries if the input can be converted into a datatype of int
        return age_int  # if can be converted to int, it will return the value. If not, the program will proceed to except ValueError
    except ValueError:  # this runs if the input is in letters, with decimal points, or with other symbols like !@#$%^ etc.
        print("\nERROR: Invalid age. Please enter whole numbers.\n")
        return False


def life_stage_classification(age_stage):
    if (0 <= age_stage <= 12):
        print("\nLife stage: Kid\n")
    elif (13 <= age_stage <= 17):
        print("\nLife stage: Teen\n")
    elif (age_stage == 18):
        print("\nLife stage: Debut\n")
    elif (19 <= age_stage <= 120):  # To be realistic, I decided to put the age limit to 120 in reference to the oldest person to live in the 21st century whose age is 118 yrs old
        print("\nLife stage: Adult\n")
    elif (age_stage >= 121):    # this will run if the input exceeds 120
        print("\nSorry. You exceeded the age limit. Cannot be classified.\n")
    elif (age_stage <= -1):     # all ages are positive values so negative inputs are restricted
        print("\nInvalid age. Less than 0 inputs are not accepted.\n")

# prompting the program to run these functions in order
display_header()
age = get_input()
valid_age = age_validation(age)
if valid_age != False:  # if the returned value for valid_age is false, the whole program will terminate or end
    life_stage_classification(valid_age) # if it is not false, it will continue to run life_stage_classification() function
