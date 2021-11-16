# Program 3
# Create a program that ask for an age of a person
# Display the life stage of the person
# 0 - 12 : Kid
# 13 -17 : Teen
# 18 : Debut
# 19 above : Adult

def display_header():
    print("\nGood day!\n\n")


def get_input():    
    age_input = input("Enter your age to classify your life stage: ")
    return age_input


def age_validation(age_try):
    try:
        age_int = int(age_try)
        return age_int
    except ValueError:
        print("\nInvalid age. Please enter whole numbers.")
        return False    

display_header()
age = get_input()
valid_age = age_validation(age)