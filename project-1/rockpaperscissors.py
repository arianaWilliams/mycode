#!/usr/bin/env python3
"""mini project creating the game rock paper scissors"""
import random

def main():
    """runtime function"""

    # create an object to hold the categories
    category = ["rock", "paper", "scissors"]

    # variable to continue playing
    play = True
    while play:
        # get user input category
        user_turn = input("Please choose (rock, paper, or scissors): ")
        user_turn = user_turn.lower()  # make user input lower case
        category_num = random.randint(0, 2)  # pick a random number between 0 and 2
        computer = category[category_num]  # get the name of the category based on the random number above

        # handles if the user chooses rock
        if user_turn == "rock":
            if category_num == 0:
                print("You chose " + user_turn + " the computer chose " + computer + ", so it's a tie")
            elif category_num == 1:
                print("You chose " + user_turn + " the computer chose " + computer + ", so you LOSE")
            elif category_num == 2:
                print("You chose " + user_turn + " the computer chose " + computer + ", so you WIN")
        # handles if the user chooses paper
        elif user_turn == "paper":
            if category_num == 0:
                print("You chose " + user_turn + " the computer chose " + computer + ", so you WIN")
            elif category_num == 1:
                print("You chose " + user_turn + " the computer chose " + computer + ", so it's a tie")
            else:
                print("You chose " + user_turn + " the computer chose " + computer + ", so you LOSE")
        # handles if the user chooses scissors
        elif user_turn == "scissors":
            if category_num == 0:
                print("You chose " + user_turn + " the computer chose " + computer + ", so you LOSE")
            elif category_num == 1:
                print("You chose " + user_turn + " the computer chose " + computer + ", so you WIN")
            else:
                print("You chose " + user_turn + " the computer chose " + computer + ", so it's a tie")
        # handles if the user doesn't choose a valid option
        else:
            print("Please enter rock, paper, or scissors")

        # handles if the player wants to play again
        play_again = input("Do you want to play again? (Y/n): ")
        if play_again.lower() == "n":
            play = False

# call main function
if __name__ == "__main__":
    main()

