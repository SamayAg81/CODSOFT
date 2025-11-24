## TASK 4
# Rock-Paper-Scissors Game
# User Input: Prompt the user to choose rock, paper, or scissors.

# Computer Selection: Generate a random choice (rock, paper, or scissors) for

# the computer.

# Game Logic: Determine the winner based on the user's choice and the

# computer's choice.

# Rock beats scissors, scissors beat paper, and paper beats rock.
# Display Result: Show the user's choice and the computer's choice.

# Display the result, whether the user wins, loses, or it's a tie.

# Score Tracking (Optional): Keep track of the user's and computer's scores for

# multiple rounds.

# Play Again: Ask the user if they want to play another round.

# User Interface: Design a user-friendly interface with clear instructions and

# feedback.


import random
'''
-1 for rock
1 for paper
0 for scissors
'''
computer = random.choice([-1, 0, -1])
youstr = input("Enter your choice:")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict =  {-1:"rock", 1:"paper", 0:"scissors"}

you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("It's a draw!")

else:
    if(computer ==-1 and you ==1):
     print("You win!")

    elif(computer ==-1 and you ==0):
     print("You Lose!")

    elif(computer ==1 and you ==-1):
     print("You Lose!")

    elif(computer ==1 and you ==0):
     print("You win!")

    elif(computer ==0 and you ==-1):
     print("You Lose!")

    elif(computer ==0 and you ==1):
     print("You win!")

    else:
     print("Something went wrong!")
