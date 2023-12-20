import re
from antlr4 import FileStream
from PasswordLexer import PasswordLexer


def main():
    input_file = "input.txt"
    input_stream = FileStream(input_file)
    lexer = PasswordLexer(input_stream)

    def is_valid_password(password):
        # Check if the password is at least 8 characters long
        if len(password) < 8:
            return False

        # Check if the password contains at least one digit
        if not any(char.isdigit() for char in password):
            return False

        # Check if the password contains at least one uppercase letter
        if not any(char.isupper() for char in password):
            return False

        # Check if the password contains at least one special character
        special_characters = r"[@#$%^&*()-=_+{}|\[;':\",.<>?/]"
        if not re.search(special_characters, password):
            return False

        # Check if the password contains no spaces
        if ' ' in password:
            return False

        # If all conditions are met, the password is valid
        return True

    # Store token texts in a list to include whitespaces
    token_texts = [token.text for token in lexer.getAllTokens()]

    # Concatenate all token texts into a single string
    password_input = ''.join(token_texts)

    # Run the validation logic once for the entire input string
    result = is_valid_password(password_input)

    if result:
        print(password_input)
        if ' ' in token_texts:
            print("Password is invalid.")
        else:
            print("Password is valid.")

    else:
        print(password_input)
        print("Password is invalid.")


if __name__ == "__main__":
    main()
