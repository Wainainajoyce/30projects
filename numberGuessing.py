import random
import math

# General tasks
# Build a number guessing game where the user selects a range(integer) giving both the upper bound and lower bound of the range
# System generates an integer and user guesses the integer in the minimum number of guesses.
"""
User inputs the lower bound and upper bound of the range - working
The compiler generates a random integer between the range and store it in a variable for future references. - working
For repetitive guessing, a while loop will be initialized. - working
If the user guessed a number which is greater than a randomly selected number, the user gets an output “Try Again! 
You guessed too high“ - working
Else If the user guessed a number which is smaller than a randomly selected number, the user gets an output “Try Again! 
You guessed too small” - working
And if the user guessed in a minimum number of guesses, the user gets a “Congratulations! ” Output.
Else if the user didnt guess the integer in the minimum number of guesses, he/she will get “Better Luck Next Time!” output.
The system should calculate the number of guesses depending on the range a user have a display that to the user each time 
they make a guess.
Maximum  number of guesses = log2(Upper bound - lower bound +1)
"""

lowerBound = int(input("Enter the starting number of your guess 'range': "))
upperBound = int(input("Enter the ending number of your guess 'range': "))
guessRange = range(lowerBound,upperBound)
numberOfGuesses = 0
maximumGuess = round(math.log2(upperBound - lowerBound + 1))

generatedNumber = random.randint(lowerBound,upperBound)


while numberOfGuesses < maximumGuess:
        numberOfGuesses += 1
        userGuess = int(input("Enter the number you want to guess in the range you entered: "))
        if userGuess > generatedNumber:
            print("Try Again! You guessed too high!")
        elif userGuess < generatedNumber:
            print("Try Again! You guessed too small!")
        
        else:
            print("Congratulations, Your guess was right!")
            break
else:
     print("You exhausted your guesses. Better Luck next time!")

print("Congratulations guys. You did it in an hour!!!")

