#Step 5

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

import hangman_words
import hangman_art

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]

word_list = ["aardvark", "baboon", "camel"]
random_word = random.choice(word_list)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

#Testing code
print(f'Pssst, the solution is {random_word}.')

#TODO-1: - Create an empty List called display.
display = []

#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

for words in random_word:
  display.append("_")
print(display)

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
  
end_game = False

while not end_game:
  guess = input('Please guess a letter\n').lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
  for position in range(len(random_word)):
    words = random_word[position]
    if guess in words:
      display[position] = guess

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
  print(display)


  #TODO-2: - If guess is not a letter in the chosen_word,
  #Then reduce 'lives' by 1. 
  #If lives goes down to 0 then the game should stop and it should print "You lose."
  if guess not in words:
    lives -= 1
    
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    
    # Originally I had lives < 0 but that doesn't work it gives 7 instead of 6 it has to be ==.
    if lives == 0:
      end_game = True
      print('You lose!')

    #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")

    #Check if user has got all letters.
  if not "_" in display:
    end_game = True
    print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    
    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
  print(stages[lives])