print("Welcome to my computer quiz!")

playing = input("Do you want to play?")

if playing.lower() != "yes":
    print("thank you for visiting")
    quit()

print("okay! lets play :)")
score = 0

answer = input("what does cpu stands for?").lower() 
if answer.lower() == "central processing unit":
    print("congrats, you are correct")
    score += 1
else:
    print("incorrect!")

answer = input("what does gpu stands for?").lower() 
if answer == "graphic processing unit":
    print("congrats, you are correct")
    score += 1
else:
    print("incorrect!")

answer = input("what does ram stands for").lower() 
if answer.lower() == "random access memory":
    print("congrats, you are correct")
    score += 1
else:
    print("incorrect!")

answer = input("what does psu stands for").lower() 
if answer == "power supply":
    print("congrats, you are correct")
    score += 1
else:
    print("incorrect!")

print("you score is " + str(score) + " congrats")
print("you percentage out of 100 is " + str((score/4)*100) + "%.")