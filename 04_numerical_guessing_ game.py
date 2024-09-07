import random

print("Welcome to the guessing game!")
choice_number = input("Enter the ceiling number of the challenge: ")

if choice_number.isdigit():
    choice_number = (choice_number)
else:
    print("Error: informed value is not numerical. Please run again and enter a number!")
    quit()

random_number = random.randint(0, choice_number)

n_choices = 0

while true:
    answer_user = input("Guess the number: ")

    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        print("Error: informed value is not numerical. Please enter a number!")
        continue

n_choices = n_choices + 1
if answer_user == random_number:
    print("You got it right!")
    break
elif answer_user > random_number:
    print("Guessed high, the number is smaller...")
else:
    print("Guess low, the number is bigger...")

    print("number of attempts: " + str(n_choices))