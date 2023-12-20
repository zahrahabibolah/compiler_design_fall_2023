from antlr4 import FileStream
from mainLexer import mainLexer
import re


def main():
    input_file = "test.txt"
    input_stream = FileStream(input_file)
    lexer = mainLexer(input_stream)




    for token in lexer.getAllTokens():

        if (token.type == 3):
            print("Found Postal Code:", token.text)

        elif (token.type == 2):
            def custom_check_national_code(code):
                if not re.match(r'^[0-9]{10}$', code):
                    return False

                for i in range(10):
                    if re.match(r'^' + str(i) + r'{10}$', code):
                        return False

                sum_value = sum((10 - i) * int(code[i]) for i in range(9))
                ret = sum_value % 11
                parity = int(code[9])

                if (ret < 2 and ret == parity) or (ret >= 2 and ret == 11 - parity):
                    print("Found Valid National Number:", code)

                return False

            custom_check_national_code(token.text)

        elif(token.type == 3):
            print("Found Postal Code:", token.text)

        elif (token.type == 1):
            print("Found Email:", token.text)

        elif (token.type == 4):
            print("Found Decimal Number:", token.text)

        elif (token.type == 5):
            print("Found Software Version:", token.text)

        elif (token.type == 6):
            print("Found Website Address:", token.text)

        elif (token.type == 8):
            # Ignore whitespace tokens
            pass


if __name__ == "__main__":
    #user_input = input("Enter the text: ")

    main()
