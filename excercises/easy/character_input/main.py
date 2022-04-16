# This could be 3-4 lines of code
# My goal was to make it as error-proof as possible

from datetime import date


def get_name():
    while True:
        user_name = input("Type in your first name: ")
        if user_name:
            return user_name.strip()
        
def get_age():
    while True:
        user_age = input("Type in your age: ")
        # Prevents submission of space
        if user_age.strip():
            return user_age.strip()
        
def get_celebrate():
     while True:
        celebrated = input("Have you celebrated birthday this year?\nY/N: ")
        if celebrated:
            if celebrated.upper() == "N" or celebrated.upper() == "Y":
                return celebrated
            
def calculate_year(user_age):
    current_year = date.today().year
    birth_year = current_year - int(user_age)
    celebrated = get_celebrate()
    year_hundred = birth_year + 100 if celebrated.upper() == "Y" else birth_year + 99
    
    return year_hundred

# Extra
def print_again(name, year):
    while True:
        reprint = input("How many times shall I re-print the results?\n0-X times: ")
        if reprint.strip():
            reprint = int(reprint)
            if reprint == 0:
                print("Alright, goodbye!")
                break
            elif reprint > 10:
                print("I'm not going to print it THAT many times. Bye!")
                break
            else:
                for _ in range(reprint):
                    print(f"Dear {name}, year {year} will be the year you turn 100.\n")
                    break

def print_result(name, year):
    print(f"Dear {name}, year {year} will be the year you turn 100.\n...")
    print_again(name, year)
    

def main():
    user_name = get_name()
    user_age = get_age() 
    calculated_year = calculate_year(user_age)
    
    print_result(user_name, calculated_year)


main()
