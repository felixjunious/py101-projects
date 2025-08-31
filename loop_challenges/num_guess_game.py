import random
num = random.randint(1,10)

guess = 0

print('Guess the number between 1-10')
print('=============================')

while guess != num:
    guess = int(input('Enter a number : '))

    if guess < num:
        print('Number is higher')
    elif guess > num:
        print('Number is lower')
    else:
        print('Correct!')