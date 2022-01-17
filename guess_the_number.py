# You ask a user to guess a number between 1 and 50.
# If they guess outside that range, you prompt with an error encouraging
# them to choose a number within the proper range.
# Whenever they guess the wrong number you ask if they want to keep playing or if they'd like to quit.
# Finally, when the user eventually guesses the right number you congratulate them
# and show the number of attempts they had.
import random

comp_choice = random.randint(1,50)
count=0
q='c'
while q=='c':
    user_input = int(input("Enter the number between 1 and 50: "))
    if user_input < 1 or user_input > 50:
        print("Wrong input!!!")
    else:
        if user_input== comp_choice:
            print("Congratulations!!!! You guessed the correct number!!!")
            print("Your guesses are {}".format(count))
            break
        elif user_input > comp_choice :
            print("Please guess the lower number!!!")
            count+=1
            q = input("Press q to quit or c to continue!!")

        elif user_input < comp_choice :
            print("Please guess the higher number!!!")
            count += 1
            q = input("Press q to quit or c to continue!!")
else:
        print("Your guesses are {}".format(count))



