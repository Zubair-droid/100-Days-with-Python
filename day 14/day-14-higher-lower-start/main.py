from art import logo, vs
from game_data import data
import random



def play_game():
    choice1 = random.choice(data)
    score = 0
    game_over = False
    while game_over != True:

        print("Welcome to 'higher-lower 🚀 ' game")
        print(logo)

        choice2 = random.choice(data)

        print(
            f"Compare A: {choice1['name']}, a {choice1['description']} from {choice1['country']}"
        )
        print(vs)
        print(
            f"Against B: {choice2['name']}, a {choice2['description']} from {choice2['country']}"
        )

        user_assume = input("Who has more followers? Type A or B: ")

        if user_assume == "A":
            if int(choice1['follower_count']) > int(choice2['follower_count']):
                score += 1
                print(f"You're right, and score is: {score}")
            elif int(choice1['follower_count']) < int(
                    choice2['follower_count']):
                print("Sorry, that's wrong")
                game_over = True
                print(f"Your score : {score}")
            else:
                print("Its a draw")
        elif user_assume == "B":
            if int(choice2['follower_count']) > int(choice1['follower_count']):
                score += 1
            elif int(choice2['follower_count']) < int(
                    choice1['follower_count']):
                print("Sorry, that's wrong")
                game_over = True
                print(f"Your score : {score}")
            else:
                print("Its a draw")
        choice1 = choice2  #This statement takes choice B to choice A in the next comparison


play_game()
