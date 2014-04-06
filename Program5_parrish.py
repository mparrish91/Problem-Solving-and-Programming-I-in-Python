#! /usr/bin/pythonw 
#CS 101 #Program 5
#Malcolm Parrish 
#mp2gb@mail.umkc.edu)
##
##PROBLEM: #This program is for Benford's Law.  The program examines the first digit ocurrences for ballot boxes in districts to look for suspicious data.  The program reads from a file, keeps track of the first digit occurences and then checks the distribution of digits in each district.
##
##ALGORITHM:

#See attached

#Open the file
def AskforFileName(prompt : str):
	while True:
		try:
			filename = input(prompt)
			return open(filename)
		except FileNotFoundError:
			print("Could not open that file.  Please check and enter another filename")

def AskforToleranceRange():
	'''Prompts user for 2 values as tolerance range.  Values are stored as low and high tol. Invalid attempts are reprompted.
	
'''
	while True:	
		try:
			range = input("Enter the tolerance range for valid values for the digit 1 \n eg 20 40 for 20 to 40% is acceptable: ")
			low_tol,high_tol = [int(i) for i in range.split(' ')]

			if low_tol <= 0 or high_tol >= 100:   #Tolerance values must be between 0 and 100
				print("The values must be between 0 and 100")
				continue

			if low_tol > high_tol:
				print("The lower tolerance value should be less than the high bound value")
				continue

			return low_tol,high_tol
	
		except ValueError:
			print("You must enter two float values.  From and To seperated by a space")

def update_dictionary(word_dict : dict, word : str, number: str) -> None:
	'''updates the dictionary with tuple including the count of the district and the count of 1s as first number in total votes

Parameters :
word_dict - Dictionary that contains a group of districts as a key and a counts tuple as values
word - Word to add a count to in the dictionary
number - the number of votes, first position is checked for 1
'''
	total = 0
	first_1 = 0
	if word not in word_dict:
		if number[0] != "1": 
			word_dict[word] = (first_1, total + 1)
		else:
			word_dict[word] = (first_1 + 1, total + 1)
	else:
		first_1, total = word_dict[word]               #Reassign to avoid assigning to 0 at the top of the loop
		if number[0] != "1": 
			word_dict[word] = (first_1, total + 1)
		else:
			word_dict[word] = (first_1 + 1, total + 1)

	return word_dict


def PrintList(word_dict : list, high : int, low : int) -> None:
	"""
	Prints out a list of the districts and the percentages that are out of the tolerance range
	Parameters :

"""
	print("Districts that have a tolerance out of value for the first digit")
	print("{:<30}{:>19}".format("District", "Perc."))
	print("="*50)
	for key in word_dict:
		percent = (word_dict[key][0] / word_dict[key][1]) * 100   #Calculates percentage
		if percent > high or percent < low:                       #Districts out of tolerance range
			print("{:.<30}{:.>20.2f}".format(key, percent))


def main():
	print("Election Results Validation")

	filehandle = AskforFileName("What is the name of the ballot file? ")
	print("\n")
	low, high = AskforToleranceRange()  #Assigns tolerance ranges from function

	word_dict = {}
	tolerance_test_dict = {}
	for line in filehandle:
		line_list = line.split()
		if len(line_list) == 3:
			tolerance_test_dict = update_dictionary(word_dict, line_list[2], line_list[0])   #Updates dictionary using function
		else:
			continue

	filehandle.close()
	print("\n")

	PrintList(tolerance_test_dict,high,low)     #Prints the districts out of the tolerance range


