password = input('New Password : ')
confirm = input('Confirm Password : ')

if password == confirm:
    print('Password changed')
else:
    if password.casefold() == confirm.casefold():
        print('Please check the cases and try again')
    else:
        print('Passwords do not match')
