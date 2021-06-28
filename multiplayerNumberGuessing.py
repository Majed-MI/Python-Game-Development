# Multiplayer Game: Number Guessing Game
import random

# function for the number input for the guess
def true_choice():
    # while loop to conitnue till wrong error
    while True:
        # try if the user gives the integer number
        try:
            # input taking from the player 1 by one
            choice = int(input())
            break
        # error handling if not integer value given
        except ValueError:
            print("Enter only integer values")
    # returning the choice input from the user
    return choice

# function for guesssing the number and taking value the random number for each player
def guess(number):
    # declaring trials as 1
    trials = 1

    # declaring choice player as the function of true choice which works taking input from each player
    choice_player = true_choice()

    # while loop to continue till the input number is same as the random number from the user
    while choice_player != number:
        # adding 1 to trials to make attempts count
        trials += 1
        # if the input number is less than the random number then
        if choice_player < number:
            print("Wrong Guess !! A greater Number again!")
            # calling function again
            choice_player = true_choice()
        # else the input number is greater than the random number
        else:
            print("Wrong Guess !! A smaller Number again")
            # calling function again
            choice_player = true_choice()

    # printing the attempts taking for guessing the number
    print(f"Correct! You took {trials} trials to guess the number {number}\n")
    # returning trials to make count
    return trials

# only applicable when under these function
if __name__ == '__main__':
    # try taking the value as integers
    try:
        a = int(input("Enter the value of A:"))
        b = int(input("Enter the value of B:"))
    # error handling if not integer given as input
    except ValueError:
        print("Please choose integer values")
        # exit the program if wrong input is given
        exit()

    # for player 1 random number declaraztion
    rand_number1 = random.randint(a,b)
    print("Player 1 :")
    print(f"Please Guess the number between {a} and {b}")
    # trial1 declaring the function of guess(number) and putting the value of random number for player 1
    # returning trial from the function guess(number) means the attempts taken by player 1 is the trials value
    trial1 = guess(rand_number1)

    # for player 2 random number declaraztion
    rand_number2 = random.randint(a,b)
    print("Player 2:")
    print(f"Please Guess the number between {a} and {b}")
    # trial1 declaring the function of guess(number) and putting the value of random number for player 1
    # returning trial from the function guess(number) means the attempts taken by player 1 is the trials value
    trial2 = guess(rand_number2)

    # for player 3 random number declaraztion
    rand_number3 = random.randint(a, b)
    print("Player 3:")
    print(f"Please Guess the number between {a} and {b}")
    # trial1 declaring the function of guess(number) and putting the value of random number for player 1
    # returning trial from the function guess(number) means the attempts taken by player 1 is the trials value
    trial3 = guess(rand_number3)

    # if the player 1 takes less attempts then he is the winner
    if(trial1<trial2 and trial1<trial3):
        print("---------------------------------------------Player 1 wins---------------------------------------------\n")
        print(f"Player 1 took {trial1} attempts and player 2 took {trial2} attempts and player 3 took {trial3} attempts")

    # If the player 2 takes less attempts then he is the winner
    elif(trial1>trial2 and trial2<trial3):
        print("---------------------------------------------Player 2 wins----------------------------------------------\n")
        print(f"Player 1 took {trial1} attempts and player 2 took {trial2} attempts and player 3 took {trial3} attempts")

    # If the player 3 takes less attempts then he is the winner
    elif (trial1 > trial3 and trial3 < trial2):
        print("---------------------------------------------Player 3 wins----------------------------------------------\n")
        print(f"Player 1 took {trial1} attempts and player 2 took {trial2} attempts and player 3 took {trial3} attempts")

    # otherwise draw
    else: 
        print("-------------------------------------------------Draw-------------------------------------------------\n")
        print(f"Player 1 took {trial1} attempts and player 2 took {trial2} attempts and player 3 took {trial3} attempts")