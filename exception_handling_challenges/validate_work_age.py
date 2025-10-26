class InvalidAgeError(Exception):
    def __init__(self):
        self.msg = 'Age should be between 18 and 60'

    def __str__(self):
        print(self.msg)

def validate_age(age):
    if 18 <= age <= 60:
        return True

    raise InvalidAgeError()

if __name__ == '__main__':

    name = input('Enter name : ')
    age = int(input('Enter age : '))

    try:
        validate_age(age)
    except InvalidAgeError as e:
        print(e)
    else:
        print('You can join work')


