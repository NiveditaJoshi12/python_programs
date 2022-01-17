import random
import math

lower_bound = int(input("Enter the lower limit: "))
upper_bound = int(input("\n Enter the upper limit: "))
num = random.randint(lower_bound, upper_bound)
count = 0
no_of_guesses = int(math.log(upper_bound-lower_bound+1,2))
print(f"You have {no_of_guesses} guesses.")
while count <= no_of_guesses:

    count += 1
    guessed_num = int(input("\n Guess the number: "))
    if guessed_num == num:
        print("Correct guess!")
        break

    elif guessed_num < num:
        print("Guess higher! Try Again! ")
        #guessed_num = int(input("\n Guess the number: "))

    elif guessed_num > num:
        print("Guess lower! Try Again!")
        #guessed_num = int(input("\n Guess the number: "))

if count > no_of_guesses:
    print("Better luck next time!")

