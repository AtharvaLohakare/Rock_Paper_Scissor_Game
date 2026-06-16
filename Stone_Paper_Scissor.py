# Stone = -1
# paper = 0
# Scissor = 1

import random

print("""
Stone
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

Paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

Scissor
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

winning_message = ("Great Job!","You Defeated the Computer!" ,"Awesome!","Victory is yours!")
losing_messages = ("Computer wins!","Better luck next time!","You lost this round!","Try again!")


print("----------------------Stone Paper Scissor----------------------")

choices = {"stone" : -1 , "paper" : 0 , "scissor" : 1}
rev_choices = {-1 : "stone" , 0 : "paper" , 1 : "scissor"}

wins = 0
losses = 0
draws = 0


while True:

    computer_choice = random.choice((-1,0,1))
    user = input("Enter Your Choice :")
    user = user.lower()

    if user not in choices:
        print("Invalid Input")
        continue
    else:
        user_choice = choices[user]

        print(f"Computer Choice is {rev_choices[computer_choice]}")
        print(f"Your Choice is {rev_choices[user_choice]}")

        if user_choice == computer_choice :
            print("Match is Draw\n")
            draws += 1

        else:
            if computer_choice == 1 and user_choice == -1:
                print(random.choice(winning_message),"\n")
                wins += 1
            elif computer_choice == 1 and user_choice == 0:
                print(random.choice(losing_messages),"\n")
                losses += 1 
            elif computer_choice == 0 and user_choice == -1:
                print(random.choice(losing_messages),"\n")
                losses += 1 
            elif computer_choice == 0 and user_choice == 1:
                print(random.choice(winning_message),"\n")
                wins += 1
            elif computer_choice == -1 and user_choice == 1:
                print(random.choice(losing_messages),"\n")
                losses += 1 
            elif computer_choice == -1 and user_choice == 0:
                print(random.choice(winning_message),"\n")
                wins += 1
            else :
                print("Incorrect Input")
            
            
    # score
    play_again = input("Play again? (Yes/No)").lower()
    if play_again != "yes":
        print("\n------ FINALSCORE ------")
        print(f"Wins   : {wins}")
        print(f"Losses : {losses}")
        print(f"Draws  : {draws}")
        print("------------------------")
        print("Thanks for Playing")
        break

    