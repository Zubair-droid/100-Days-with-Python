from art import logo
print(logo)

import random

random_no = random.randint(1,100)


print("I'm thinking a number between 1 and 100. Can you guess")
level = input("Select a level. Type easy/ normal/ hard : \n")

if level == "easy":
  attempts = 10
elif level == "hard":
  attempts = 5
elif level == "normal":
  attempts = 8


def guess_number(attempts):
  for i in range(1, attempts + 1):
    user_guess = int(input(f"Guess the number. You have {attempts} attempts left\n"))
    attempts -= 1
    #print(attempts)
    if user_guess > random_no:
        print("Too high")
    elif user_guess < random_no:
      print("Too low")
    elif user_guess == random_no:
      print(f"Yay, You got it 😎. The number was {random_no} ")
      break
  if attempts == 0 and user_guess != random_no: 
      print("You ran out of attempts 😪.Lose")
       
     
     
guess_number(attempts)