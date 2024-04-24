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
game_images = [rock,paper,scissors]

user_choice = int(input("What is your choice ? Type 0 for Rock, 1 for Paper, 2 For Scissors. \n"))
print(game_images[user_choice])

computer_choice = random.randint(0,2)
print("Computer choice :")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0 :
    print("You typed an an invaild number,you lose! Better luck Next time")
elif user_choice == 0 and computer_choice == 2 :
    print("Congratulations ,You won!")
elif computer_choice == 0 and user_choice == 2 :
    print("Oops You lose.Better luck next time.")
elif computer_choice > user_choice :
    print("Oops You lose.Better luck next time.")
elif user_choice > computer_choice :
    print("Congratulations ,You won!")
elif computer_choice == user_choice :
    print("Ooh,It's draw match")
