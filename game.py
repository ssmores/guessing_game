# Put your code here
import random 

print "Greetings!"

player_name = raw_input("What is your name friend? ")

randomly_generated_number = random.randint(1, 100)

player_guess = int(raw_input("Guess a number between 1 and 100. "))

# while player_guess != randomly_generated_number: