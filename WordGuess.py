import random
import time

print("Initializing...")
time.sleep(2)               # make it seem like the computer is actually doing something ;)

answer = ""
guess = ""
user_points = 0
computer_points = 0
word_length = 0         # initialize all the variables

print("Welcome to the word guessing game! Now with 100% uncertainty.")

while True:

    print("Finding word...")
    time.sleep(1)
    print("Calculating whether it has odd or even length...")
    time.sleep(2)
    word_length = random.randint(1, 20)     # generate a random word length between 1 and 20 inclusive
    if word_length%2 == 0:              # check for even
        answer = "even"
    else:
        answer = "odd"
    print("Done!")
    time.sleep(1)

    guess = input("Is my word of odd or even length? ").lower()     # get a guess from the user
    if guess == "even" or guess == "odd":       # catch unexpected input
        if guess == answer:                  # check guess against answer and increment points
            print("You guessed correct! Have a point.")
            user_points += 1
        else:
            print("You guessed wrong! I get a point.")
            computer_points += 1
    else:
        print("You broke it. exiting...")
        break

    print("Now to turn it around: Please think of a word.")
    time.sleep(4)
    print("Guessing...")
    guess = random.randint(0, 1)            # get a 0 or 1 randomly to represent odd and even
    if guess == 1:
        guess = "even"          # assign odd or even to guess
    else:
        guess = "odd"
    time.sleep(2)
    print("OK, i have my guess.")

    answer = input("Please enter the number of letters your word has: ")    # get the number of letters from the user
    if answer.isdecimal():                      # catching unexpected input
        answer = int(answer)            # storing the number as an integer
    else:
        print("That's not a whole number. You broke it, please try again.")
        continue

    if answer%2 == 0:       # check and assign answer
        answer = "even"
    else:
        answer = "odd"

    if guess == answer:         # check guess against answer and increment points
        print("I guessed correct! I get a point.")
        computer_points += 1
    else:
        print("I guessed wrong! You get a point.")
        user_points += 1
    print("User: ", user_points)
    print("Computer: ", computer_points)

    response = input("Keep playing? ").lower()       # check whether the user wants to keep playing, break out if no
    if response == "yes":
        continue
    elif response == "no":
        break
    else:
        print("You broke it. exiting...")     # call out if the user tries anything funny
        break

print("Thank you for playing the word guessing game!")
print("")
print("Final score:")
print("User: ", user_points)
print("Computer: ", computer_points)        # print a final message and give the user time to read it
time.sleep(5)




















