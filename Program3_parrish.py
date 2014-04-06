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



while PlayAgain_bool == True:
	words_str = open("dictionary.txt").readlines()

	word_str = random.choice(words_str).strip() #select 1 at random, remove \n at end
	
	word_list = list(word_str)
	guessed_list = "-" * len(word_list)
	print("The word is", len(word_str), "letters long")
	
	win_bool = False
	guesses_int = 7
	guessed_letters_str = ""
	letters_available_str = "ABCDEFGHIJKLMNOPQRSTUVYXYZ"
	while win_bool == False or guesses_int < 7:
		print("You have", guesses_int, "guesses remaining")
		print("Word = ", guessed_list)
		print("Guessed: ", guessed_letters_str)
		print("Available: ", letters_available_str)
		
		guess_str = input("Please guess a letter").upper()
		if not guess in "ABCDEFGHIJKLMNOPQRSTUVYXYZ":
			print("Please guess a letter")
			continue #reprompt user for valid input
		
		guessed_letters_str = guessed_letters_str + guess_str
		letters_available_str = letters_available_str - guessed_letters_str

		if guess in word_list:
			for i, guess in enumerate(word_list):
				guessed_list[i] = guess
			else:
				guesses_int -= 1
				print("Sorry that letter is not in the word")

		
		if guessed_list == wordlist:
			print("You have won the game")
			win = True
			break
	
	if win == True:
		print("Congratulations you Won")
	else:
		print("Game Over")
		print("The secret word is", word_str)

	
	PlayInput_str = input("Do you want to play again? (Y/N) ").upper()
	if PlayInput_str == "N":
		PlayAgain = False

	
		
	
	
				
		
		