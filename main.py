def encode(new_password):  # Jack Berman
    new_password = ""  # encodes user password and adds 3 to each value place in the string
    for value in new_password:
        new_digit = str((int(value) + 3) % 10)
        new_password = new_password + new_digit
    return new_password


def main():
    while True:
        print("Menu\n----------\n1.  Encode\n2.  Decode\n3.  Quit")  # prints menu for program
        print()
        user_input = int(input("Please enter an option: "))

        if user_input == 1:  # runs the encode function and stores its value
            new_password = (input("Please enter your password to encode: "))
            encode(new_password)
            print("Your password has been encoded and stored!")
            print()
        elif user_input == 2:  # returns original and encoded password
            pass
        elif user_input == 3:  # quits the program
            break


if __name__ == "__main__":
    main()
