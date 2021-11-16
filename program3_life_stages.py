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
        print("\nERROR: Invalid age. Please enter whole numbers.\n")
        return False    


def life_stage_classification(age_stage):
    if (0 <= age_stage <= 12):
        print ("\nLife stage: Kid\n")
    elif (13 <= age_stage <= 17):
        print ("\nLife stage: Teen\n")
    elif (age_stage == 18):
        print ("\nLife stage: Debut\n")
    elif (19 <= age_stage <= 150):
        print ("\nLife stage: Adult\n")
    elif (age_stage >= 151):
        print("\nSorry. You exceeded the age limit. Cannot be classified.\n")
    elif (age_stage <= -1):
        print("\nInvalid age. Less than 0 inputs are not accepted.\n")

display_header()
age = get_input()
valid_age = age_validation(age)
if valid_age != False:
    life_stage_classification(valid_age)