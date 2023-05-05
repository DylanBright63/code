print("Welcome To My Game")

playing = input("Do you want to play? ")

if playing != "Yes":
    quit()

print("Okay! lets's Play :)")

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print('Correct')
else:
    print("Incorrect")
    score += 1

answer = input("What does Gpu stand for? ")
if answer == "Graphics processing unit":
    print('Correct')
else:
    print("Incorrect")
    score += 1

answer = input("What does RAM stand for? ")
if answer == "Random Access memory":
    print('Correct')
else:
    print("Incorrect")
    score += 1

print ("You got " + str(score) + "question correct!")

