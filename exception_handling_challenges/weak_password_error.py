import re

class WeakPasswordError(Exception):
    def __init__(self, msg=''):
        self.msg = msg

    def __str__(self):
        return self.msg


def is_strong(password):
    msg = 'Password must contain at least '

    if len(password) < 8:
        raise WeakPasswordError(msg + '8 characters')

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = bool(re.search(r'[^A-Za-z0-9]', password))

    if not has_upper:
        raise WeakPasswordError(msg + 'one uppercase letter')

    if not has_lower:
        raise WeakPasswordError(msg + 'one lowercase letter')

    if not has_digit:
        raise WeakPasswordError(msg + 'one digit')

    if not has_special:
        raise WeakPasswordError(msg + 'one special character')

    return True, "Password is strong"


password = input('Enter Password: ')

try:
    valid, message = is_strong(password)
except WeakPasswordError as e:
    print(e)
else:
    print(message)
