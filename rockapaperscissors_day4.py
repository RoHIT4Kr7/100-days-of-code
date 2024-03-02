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

user_choices = [rock, paper, scissors]
computer_choices = [rock, paper, scissors]

user_input = int(input("What do you choose? Type 0 for rock, 1 for paper, and 2 for scissors: "))

computer_choice = random.randint(0, 2)

if user_input == computer_choice:
    print("It's a tie!")
elif user_input == 0 and computer_choice == 2 or \
     user_input == 1 and computer_choice == 0 or \
     user_input == 2 and computer_choice == 1:
    print("You win!")
else:
    print("You lose!")

print(f"Your choice:\n{user_choices[user_input]}")
print(f"Computer's choice:\n{computer_choices[computer_choice]}")
