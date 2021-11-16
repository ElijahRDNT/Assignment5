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

display_header()
age = get_input()