# words = open("word.txt","r")

# word_bank = words.read()

# trial_count = 0
# word_count = 0
# misplaced_letters = []


# while True:
#     word = input("Enter a 5 letter word: ")
#     if word in word_bank:
#         if len(word) == 5:
#             print(f"You've entered the correct word: {word}")
#             word_count +=1
#             if word_count == 5:
#                 print("You've completed the game")

#         else:
#             print("You've entered the correct word without the correct word_length")
#             trial_count +=1
#             if trial_count == 5:
#                 print("You've exceeded your trial count!!")
#                 break
#     for letter in word:
#         if letter == letter:
#             print(letter)
#         else:
#             letter.append(misplaced_letters)      
#     # else:
#     #     print(f"You've entered an incorrect word '{word}', please enter the correct word")
#     #     trial_count+=1
#     #     if trial_count == 5:
#     #         print("You've exceeded your trial count!!")
#     #         break


# Solution
'''Based on the rules of the game, there are some key pieces of game information that we want to track to keep the player informed:

    The misplaced letters in the players guess
    The incorrect letters in the players guess
    The max number of turns we will allow
    The number of turns the player has currently made
'''

import random
game_title = "Word Raider"

# Set up the list of words to choose from
word_bank = []
with open("word.txt") as word_file:
    for line in word_file:
        word_bank.append(line.rstrip().lower())

# Pick a random word from the list
word_to_guess = random.choice(word_bank)

# Set up the game variables
misplaced_guesses = []
incorrect_guesses = []
max_turns = 5
turns_taken = 0

# Display the initial game state
print("Welcome to", game_title)
print("The word has", len(word_to_guess), "letters.")
print("You have", max_turns - turns_taken, "turns left.")

while turns_taken < max_turns:
    # Get the player's guess
    guess = input("Guess a word: ").lower()

    # Check if the guess length equals 5 letters and is all alpha letters
    if len(guess) != len(word_to_guess) or not guess.isalpha():
        print("Please enter 5-letter word.")
        continue

    # Check each letter in the guess against the word's letters
    index = 0
    for c in guess:
        if c == word_to_guess[index]:
            print(c, end=" ")
            if c in misplaced_guesses:
                misplaced_guesses.remove(c)
        elif c in word_to_guess:
            if c not in misplaced_guesses:
                misplaced_guesses.append(c)
            print("_", end=" ")
        else:
            if c not in incorrect_guesses:
                incorrect_guesses.append(c)
            print("_", end=" ")
        index += 1
    print("\n")
    print("Misplaced letters: ", misplaced_guesses)
    print("Incorrect letters: ", incorrect_guesses)
    turns_taken += 1

    # Check if the player has won
    if guess == word_to_guess:
        print("Congratulations, you win!")
        break  # Exit the loop when the player wins

    # Check if the player has lost
    elif turns_taken == max_turns:
        print("Sorry, you lost. The word was", word_to_guess)
        break  # Exit the loop when the player loses


    # Display the number of turns left and ask for another guess
    print("You have", max_turns - turns_taken, "turns left.")

 

