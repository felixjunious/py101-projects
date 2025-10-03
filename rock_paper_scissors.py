import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_hand = int(input('What do you choose? type 0 for Rock, 1 for Paper or 2 for Scissors'))

computer_hand = random.randint(0, 2)

if user_hand == computer_hand:
    print("It's a draw!")
elif (user_hand == 0 and computer_hand == 2) or \
     (user_hand == 1 and computer_hand == 0) or \
     (user_hand == 2 and computer_hand == 1):
    print("You win!")
else:
    print("You lose!")



