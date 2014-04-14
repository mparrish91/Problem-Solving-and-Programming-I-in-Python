import string



def IsLengthValid()-> list:
	valid_length_list = []
	file_handle = open("dictionary.txt")
	for word in file_handle:
		word = word.strip()
		valid_length_list.append(len(word))

	return valid_length_list



def AskforWordLength(valid_length_list : list) -> int:
	Again = True
	while Again:
		letters_guess_int = int(input("Welcome to Hangman. How many letters are in secret word? "))
		if letters_guess_int < 0: 
			print("Please enter a number greater than 0")
		elif letters_guess_int not in valid_length_list :
			print("Sorry no word of that length exists in the dictionary")   
		else:
			Again = False

	return letters_guess_int


def validTry():
	Again = True
	while Again:
		guesses_int = int(input("How many guesses [1+]? "))
		if guesses_int < 0:
			print("Please enter a number greater than 0")
		else:
			Again = False

	return guesses_int


def make_mask(word : str, word_list : list, mask : list, letter : chr) -> list:
	'''Fill in the position of user guess
'''

	if letter in word:
		for i in range(len(word_list)):
			if word_list[i] == letter:
				mask[i] = letter

	return mask





def main():
	file_handle = open("dictionary.txt")

	letters_available_list = list(string.ascii_lowercase)
	guessed_letters_str = ""
	win_bool = False
	cheat_dict = {}	
	word_family_list = []
	word_list = []


	test_list = IsLengthValid() 
	word_length_int = AskforWordLength(test_list)       #Prompt the user for word length
	print_count = input("Do you want to print the count of how many words remain [Y/N]? ").upper()	 #Prompt for running total of remaining words
	guesses_int = validTry()							#Prompt for number of guesses
	

	for word in file_handle:
		word = word.strip()
		if len(word) == word_length_int:
			word_list.append(word)


	while win_bool == False and guesses_int > 0:                    	#Single game loop

		#Create mask and word as a list for make_mask function
		for word in word_list:
			mask = list(len(word) * "-")
			wordas_list = list(word)

		
		print("You have", guesses_int, "guesses left.")
		print("Letters chosen:", guessed_letters_str)
		

		#Prompt for a single letter guess, reprompting until user enters a letter they haven't guessed yet
		Again = True
		while Again:
			print("Choose one of the following: ", ' '.join(letters_available_list))
			letter_chr = input("--> ")
			if letter_chr.isalpha() == False:
				print("Please guess a valid letter")
				continue #reprompt user for valid input
			elif letter_chr not in letters_available_list:
				print("Please guess an available letter")
				continue #reprompt user for valid input
			else:
				Again = False


		
		guessed_letters_str = guessed_letters_str + letter_chr
		letters_available_list.remove(letter_chr)  # Remove guessed letters from the available list

		


		#Cheat section

		mask_str = "".join(make_mask(word, wordas_list, mask, letter_chr))          #join returned list to form string

		#Add the family to the dictionary
		try:
			cheat_dict[mask_str].append(word)   
		except KeyError:
			cheat_dict[mask_str] = [word]




		#Find the family with the most words(longest length)

		for key in cheat_dict:                                        
			inverse = [(v, k) for k, v in cheat_dict.items()]                     #convert dictionary to list of tuples(easier to work with)

		for i in inverse:
			test_max = 0
			if len(i[0]) > test_max:
				test_max = len(i[0])
			mask_filled = i[1]
			holder = i


		print("Word = ", mask_filled)

		#To show the count of how many words remain
		if print_count == "Y":
			number_of_words = test_max  
			print("{} words remaining.".format(number_of_words)) 


		#Reassign the wordlist to the new wordfamily
		word_list = holder[0]

		if letter_chr in mask:
			print("Word = ", mask_filled)
		else:
			guesses_int -= 1
			print("Sorry, {} is not present.".format(letter_chr))
			print("Word = ", mask_filled)


		if "-" not in mask_filled: 
			print("You have won the game")
			win = True
			break


	if win == True:
		print("Congratulations you correctly guessed {} and still had {} guesses left over!".format(secret_word, guesses))
	else:
		print("Game Over")


		#select a word at random from the family and choose as hangman word
		print("The secret word is", cheat_dict[mask_filled][0])



main()







