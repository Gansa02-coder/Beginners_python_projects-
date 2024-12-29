import random

top_of_range = input("type a number :")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("please type a number larger than next time.")
        quit()
else:
    print("please type a number, not a alphabets or special characters on the next time.")
    quit()

random_number = random.randint(1,top_of_range)
guesses = 0

while True:
    guesses +=1
    user_guess = input("make a guess :")
    if user_guess.isdigit():
        user_guess = int(user_guess)

        if user_guess <= 0:
            print("please type a number larger than 0.")
            continue
    else:
        print("please type a number, not a alphabets or special characters on the next time.")
        quit()


    if user_guess == random_number:
        print("you got it...!")
        break

    elif user_guess >random_number:
        print("you were above the number")
    else:
        print("you were below the number...!")

print("you got it " + str(guesses)+" guesses..!")
