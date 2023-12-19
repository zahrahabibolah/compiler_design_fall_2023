import re
from antlr4 import FileStream
from mainLexer import mainLexer
from antlr4 import InputStream
import re


def main():
    input_file = "test.txt"
    input_stream = FileStream(input_file)
    lexer = mainLexer(input_stream)

    def custom_check_national_code(input_file):
        # Extract sequences of 10 digits
        national_code_pattern = re.compile(r'\b\d{10}\b')
        national_codes = national_code_pattern.findall(input_file)

        for code in national_codes:
            if not re.match(r'^[0-9]{10}$', input_file):
                return False
            else:
                for i in range(10):
                    if re.match(r'^' + str(i) + r'{10}$', input_file):
                        return False
                    else:
                        sum_value = sum((10 - i) * int(input_file[i]) for i in range(9))
                        ret = sum_value % 11
                        parity = int(input_file[9])
            if (ret < 2 and ret == parity) or (ret >= 2 and ret == 11 - parity):
                return True

        return False

    for token in lexer.getAllTokens():
        if (token.type == 2):
            if custom_check_national_code(input_file) is True:
                national_code_pattern = re.compile(r'\b\d{10}\b')
                national_number = national_code_pattern.findall(input_file)
                postal_code_pattern = re.compile(r'\b0[1-9][013-9]{9}\b')
                print("Found Valid National Number:", token.text)
            elif(token.type == 3):
                print("Found Postal Code:", token.text)
                # Handle the case when the national code is not valid
                national_number = []
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
