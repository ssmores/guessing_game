# Put your code here
import random 

print "Greetings!"

player_name = raw_input("What is your name friend? ")

randomly_generated_number = random.randint(1, 100)

player_guess = int(raw_input("Guess a number between 1 and 100. "))

while player_guess != randomly_generated_number:
    
    if player_guess < 1 or player_guess > 100:
        print "Try again, between 1 and 100 only."
        player_guess = int(raw_input("Guess a number between 1 and 100. ")) 
    elif player_guess > randomly_generated_number:
        print "You are too high, try again."
        player_guess = int(raw_input("Guess a number between 1 and 100. "))
    elif player_guess < randomly_generated_number:
        print "You are too low, try again."
        player_guess = int(raw_input("Guess a number between 1 and 100. "))


print "Good job, you did it!"