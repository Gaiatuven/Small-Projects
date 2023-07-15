import string
import secrets


def contains_upper(password):
    """checks if password contains upper case"""
    for char in password:
        if char.isupper():
            return True
    return False


def contains_symbols(password):
    """checks if password contains symbols"""
    for char in password:
        if char in string.punctuation:
            return True
    return False


def generate_password(length, symbols, uppercase):
    """generate new password, from password and symbols in string"""
    combination = string.ascii_lowercase + string.digits

    if symbols:
        combination += string.punctuation
    if uppercase:
        combination += string.ascii_uppercase

    combination_length = len(combination)
    new_password = ''

    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]
    return new_password


if __name__ == '__main__':
    for i in range(1, 6):
        new_pass = generate_password(length=10, symbols=True, uppercase=False)
        specification = f'UPPERCASE: {contains_upper(new_pass)}, SYMBOLS: {contains_symbols(new_pass)}'

        print(f'{i} -> {new_pass} - {specification}')
