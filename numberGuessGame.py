import random
list= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,
    37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,
    70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
n = random.choice(list)
number_of_guesses = 1
print("Number of Guesses is Limited to 9 times Only")
print("The Number is between 1 to 100")
print("Here You Go!")
while(number_of_guesses<=9):
    guess_number = int(input("Guess The Number: "))
    if(guess_number>n):
        print("You have entered Greater number.")
        print("Please enter smaller number")
    elif(guess_number<n):
        print("You have entered less number.")
        print("Please enter bigger number")
    else:
        print("Wow! You Win! ")
        print(number_of_guesses,"No. of Guesses you took to finish")
        break
    print(9-number_of_guesses,"No. of Guesses left")
    number_of_guesses = number_of_guesses + 1

    if(number_of_guesses>9):
        print("Game Over!")