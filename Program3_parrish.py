#! /usr/bin/pythonw
##CS 101
##Program 2
##Malcolm Parrish
##mp2gb@mail.umkc.edu)
##
##PROBLEM: #This program is for the Hangman game.  The program selects a word at random from a dictionary file and then gives the user 7 attempts to guess the word.
##
##ALGORITHM: See separate file




import random
PlayAgain_bool = True

# Outer loop to allow the user to play again

while PlayAgain_bool == True:
    words_str = open('dictionary.txt').readlines()

    word_str = random.choice(words_str).strip()  # select 1 at random, remove \n at end

    word_list = list(word_str)
    guessed_list = list('-' * len(word_list))
    print("The word is", len(word_str), "letters long.")

    win_bool = False
    guesses_int = 7
    guessed_letters_str = ''
    letters_available_list = [
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z',
        ]

    # Inner single game loop
    while win_bool == False or guesses_int > 0:
        print("You have " + str(guesses_int) + " guesses remaining.")
        print("Word = "  + ' '.join(guessed_list))
        print("Guessed: " + guessed_letters_str)
        print("Available: " + ''.join(letters_available_list))

        guess_char = input('Please guess a letter: ').upper()

        # Check if valid guess
        if not guess_char in letters_available_list:
            print("Please guess a valid letter")
            continue  # reprompt user for valid input
        guessed_letters_str = guessed_letters_str + guess_char
        letters_available_list.remove(guess_char)  # Remove guessed letters from the available list

        # Check if guess is in the chosen word
        if guess_char.lower() in word_str:
            for i in range(len(word_list)):
                if word_list[i] == guess_char.lower():
                    guessed_list[i] = guess_char.lower()
        else:

            guesses_int -= 1
            print("Sorry, that letter is not present")
        if guessed_list == word_list:
            print("You have won the game")
            win_bool = True
            break

    if win_bool == True:
        print("Congratulations you Won")
        print("The secret word is: ", word_str)
    else:
        print("Game Over")
        print("The secret word is: ", word_str)

    # If the user wants to play again re-enter top loop

    PlayInput_str = input("Do you want to play again? (Y/N) ").upper()
    if PlayInput_str.upper() == 'N':
        PlayAgain = False

	
		
	
	
				
		
		
