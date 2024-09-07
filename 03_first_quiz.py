print("Welcome to the first quiz!")
answer_user = input("Do you want to play? (Yes/No) ")
print(answer_user)

if answer_user != "Yes":
    quit()

score = 0

print("Starting...")
print("Who developed the game Grand Theft Auto (GTA)? \n (A) Rockstar Games \n (B) Ubisoft \n (C) Activision \n (D) Electronic Arts \n")
answer_1 = input("Response: ")

if answer_1 == "A":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

print("What is the name of the protagonist of the game GTA San Andreas? \n (A) Carlos John \n (B) Carl Johnson \n (C) Carl Jaqueline \n (D) Carlos Johnson \n")
answer_2 = input("Response: ")

if answer_2 == "B":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

print("What year was GTA San Andreas released? \n (A) 2007 \n (B) 2001 \n (C) 2010 \n (D) 2004 \n")
answer_3 = input("Response: ")

if answer_3 == "D":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

print(f"Quiz is over...Your score is: {score}/3")

