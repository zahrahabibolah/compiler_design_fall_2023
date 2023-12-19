import re

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
        return True

    return False

# Example usage
national_code = input("Enter the national code: ")

if custom_check_national_code(national_code):
    print("Valid national code.")
else:
    print("Invalid national code.")
