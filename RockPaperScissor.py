import random
list = ['r','p','s']
chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0

print("\t \t \t Rock,Paper,Scissor Game\n \n")
print("r for Rock \n p for Paper\n s for Scissor \n")

while (no_of_chance < chance):
    inp = input("Rock, Paper, Scissor: ")
    rand = random.choice(list)

    if inp == rand:
        print("Tie! Both 0 point to each \n")
    # user hits rock and computer paper
    elif inp == 'r' and rand == 'p':
        computer_point = computer_point + 1
        print(f"Your guess is {inp} and Computer guess is {rand}")
        print("Computer wins 1 point")

        print(f"Computer point is {computer_point} and Your point is {human_point} \n")
    # user hits rock and computer scissor
    elif inp == 'r' and rand == 's':
        human_point = human_point + 1
        print(f"Your guess is {inp} and Computer guess is {rand}")
        print("You win 1 point")
        print(f"Computer point is {computer_point} and Your point is {human_point} \n")
    # user hits paper and computer scissor
    elif inp == 'p' and rand == 's':
        computer_point = computer_point + 1
        print(f"Your guess is {inp} and Computer guess is {rand}")
        print("Computer wins 1 point")
        print(f"Computer point is {computer_point} and Your point is {human_point} \n")
    # user hits paper and computer rock
    elif inp == 'p' and rand == 'r':
        human_point = human_point + 1
        print(f"Your guess is {inp} and Computer guess is {rand}")
        print("You win 1 point")
        print(f"Computer point is {computer_point} and Your point is {human_point} \n")
    # user hits scissor and computer rock
    elif inp == 's' and rand == 'r':
        computer_point = computer_point + 1
        print(f"Your guess is {inp} and Computer guess is {rand}")
        print("Computer wins 1 point")
        print(f"Computer point is {computer_point} and Your point is {human_point} \n")
    # user hits scissor and computer paper
    elif inp == 's' and rand == 'p':
        human_point = human_point + 1
        print(f"Your guess is {inp} and Computer guess is {rand}")
        print("You win 1 point")
        print(f"Computer point is {computer_point} and Your point is {human_point}")

    else:
        print("You have entered wrong input")

    no_of_chance =no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance}")

print("Game Over")
if computer_point == human_point:
    print("Tie!")

elif computer_point > human_point:
    print("Computer Win and You lose")

else:
    print("You Win and Computer lose")

print(f"Your point is {human_point} and computer point is {computer_point}")