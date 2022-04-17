def get_number():
    while True:
        user_number = input("Tell me a whole number and I will tell you whether it is even or odd.\nYour number: ")
        # Not going to check for floats
        # If user enters just space, loop continues
        if user_number.strip():
            # Extra
            if int(user_number) % 4 == 0:
                print("Cheeky buggar!")
                break
            elif int(user_number) % 2 == 0:
                print("Your number is even.")
                break
            else:
                print("Your number is odd.")
                break

def num_check():
    num = input("Tell me a number to be divided: ")
    check = input("Tell me a number to divide by: ")

    mod = int(num) % int(check)
    res = round(int(num) / int(check), 1)

    if mod > 0:
        print(f"Number {num} is not evenly divided by {check}.")
        print(f"{num} / {check} = {res}")
    else:
        print(f"Number {num} is evenly divided by {check}.")
        print(f"{num} / {check} = {res}")  

def main():
    get_number()
    num_check()

main()