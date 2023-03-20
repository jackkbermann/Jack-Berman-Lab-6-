def encode(user_password):  # Jack Berman
    encoded_password = ""  # encodes user password and adds 3 to each value place in the string
    for value in user_password:
        new_digit = str((int(value) + 3) % 10)
        encoded_password = encoded_password + new_digit
    return encoded_password

# hhhhhhhhwefwgrg
def main():
    while True:
        print("Menu\n----------\n1.  Encode\n2.  Decode\n3.  Quit")  # prints menu for program
        print()
        user_input = int(input("Please enter an option: "))

        if user_input == 1:  # runs the encode function and stores its value
            user_password = (input("Please enter your password to encode: "))
            encode(user_password)
            print("Your password has been encoded and stored!")
            print()
        elif user_input == 2:  # returns original and encoded password
            pass
        elif user_input == 3:  # quits the program
            break


if __name__ == "__main__":
    main()
