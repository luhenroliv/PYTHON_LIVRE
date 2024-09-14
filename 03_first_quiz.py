print("Welcome to the first quiz!")
answer_user = input("Do you want to play? (Yes/No) ")
print(answer_user)

if answer_user != "Yes":
    quit()

score = 0

print("Starting...")
print("In which year was the Atari company founded? \n (A) 1972 \n (B) 1975 \n (C) 1981 \n (D) 1998 \n")
answer_1 = input("Response: ")

if answer_1 == "A":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

print("Who is the Jedi Master who trains Luke Skywalker in Star Wars: Episode V - The Empire Strikes Back? \n (A) Obi-Wan Kenobi \n (B) Yoda \n (C) Luminara Unduli \n (D) Chewbacca \n")
answer_2 = input("Response: ")

if answer_2 == "B":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

print("What is the first title published by J.R.R. Tolkien? \n (A) The Silmarillion \n (B) The Fellowship of the Ring \n (C) Unfinished Tales \n (D) The Hobbit \n")
answer_3 = input("Response: ")

if answer_3 == "D":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

print(f"Quiz is over...Your score is: {score}/3")
