import random

user_points = 0
computer_points = 0


options = ["r", "s", "p"]


while true:
    user_choice = input("Choose R(Rock)/S(Scissors)/P(Paper) or Q for quit.").lower()

    if user_choice == 'q':
        break

if user_choice not in options:
    continue

    computer_choice = random.randint(0, 2)
    # 0: R, 1: S, 2: P
    computer_option = options[computer_choice]

print("The computer chose " + computer_option)

    if user_choice == computer_option
        print("Draw!")

    elif user_choice == "r" and computer_option == "s":
        print("You win!")
        user_points = user_points + 1

    elif user_choice == "p" and computer_option == "r":
        print("You win!")
        user_points = user_points + 1

    elif user_choice == "ps" and computer_option == "p":
        print("You win!")
        user_points = user_points + 1

else:
    print("You loose!")
    computer_points = computer_points + 1

print("Your score ": + str(user_points))
print("Computer score " + str(computer_points))

if computer_points > user_points:
    print("Defeat!")
elif computer_points == user_points:
    print("Draw!")
else:
    print("Victory!!!")

print("Goodbye!")