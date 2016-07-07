# Put your code here
import random 

print "Greetings!"

player_name = raw_input("What is your name friend? ")

randomly_generated_number = random.randint(1, 100) 

player_guess = raw_input("Guess a number between 1 and 100. ")

# Unfinished function where we wanted to try the try function. 
# def is_an_integer(guess): 
#     player_guess = raw_input("Guess a number between 1 and 100. ")
#     try:
#         type(player_guess) == int

#     except Exception, e:
#         raise e


while player_guess != randomly_generated_number:
    
    if player_guess < 1 or player_guess > 100:
        print "Try again, between 1 and 100 only this time."
        player_guess = int(raw_input("Guess a number between 1 and 100. ")) 
    elif player_guess > randomly_generated_number:
        print "You are too high, try again."
        player_guess = int(raw_input("Guess a number between 1 and 100. "))
    elif player_guess < randomly_generated_number:
        print "You are too low, try again."
        player_guess = int(raw_input("Guess a number between 1 and 100. "))


print "Good job, you did it!"