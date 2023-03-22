def encode(password):  # Jack Berman
    new_password = ""  # encodes user password and adds 3 to each value place in the string
    for value in password:
        new_digit = str((int(value) + 3) % 10)
        new_password = new_password + new_digit
    return new_password

def decode(code):
    orig_password = ""
    array = [int(i) for i in str(code)]
    for i in array:
        i -= 3
        a = str(i)
        orig_password += a
    return orig_password

def main():
    while True:
        print("Menu\n----------\n1.  Encode\n2.  Decode\n3.  Quit")  # prints menu for program
        print()
        user_input = int(input("Please enter an option: "))

        if user_input == 1:  # runs the encode function and stores its value
            password = (input("Please enter your password to encode: "))
            code = encode(password)
            print("Your password has been encoded and stored!")
            print()
        elif user_input == 2:  # returns original and encoded password
            orig_password = decode(code)
            print(f"The encoded password is {code} and the original password is {orig_password}")
            print()
        elif user_input == 3:  # quits the program
            break


if __name__ == "__main__":
    main()
