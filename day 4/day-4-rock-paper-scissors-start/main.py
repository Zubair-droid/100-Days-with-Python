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

You_chose = input("What do you choose ?,Type 0 for rock, 1 for paper or 2 for scissors \n")
print("You chose \n")
if You_chose == "0":
  print(rock)
elif You_chose =="1":
  print(paper)
elif You_chose == "2":
  print(scissors)
else:
  print("Invalid")


print("Computer chose")


choices = [paper, scissors, rock]

random_choices = random.randint(0, 2)

computer_chose = choices[random_choices]

print(computer_chose)

if You_chose == "0" and computer_chose == scissors:
  print("You Win")
elif You_chose == "0" and computer_chose == rock:
  print("Its a tie")
elif You_chose == "0" and computer_chose == paper:
  print("You Lose")

if You_chose == "1" and computer_chose == paper:
  print("Its a tie")
elif You_chose == "1" and computer_chose == rock:
  print("You Win")
elif You_chose == "1" and computer_chose == scissors:
  print("You Lose")

if You_chose == "2" and computer_chose == scissors:
  print("Its a tie")
elif You_chose == "2" and computer_chose == paper:
  print("You Win")
elif You_chose == "2" and computer_chose == rock:
  print("You Lose")