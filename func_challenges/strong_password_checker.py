import re

def is_strong(password):
    msg = "Password must contain at least"
    if len(password) < 8:
        return False, msg + "8 characters long"

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = bool(re.search(r'[A-Za-z0-9]', password))

    if not has_upper:
        return False, msg + "one uppercase letter"

    if not has_lower:
        return False,  msg + "one lowercase letter"

    if not has_digit:
        return False, msg + "one digit"

    if has_special:
        return False, msg + "one special characters"

    return True, "Password is strong"

password = input('Enter Password : ')

valid, message = is_strong(password)
print(message)