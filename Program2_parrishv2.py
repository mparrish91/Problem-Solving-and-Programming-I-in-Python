




#! /usr/bin/pythonw
##CS 101
##Program 2
##Malcolm Parrish
##mp2gb@mail.umkc.edu)
##
##PROBLEM: Write a Python program for the Pig dice game.  The game is between the computer and the user.  The program allows users to roll or hold.  After each turn an amount is added to the pot and the user has the option to continue rolling or hold.  It takes 50 to win.  If user or computer rolls a 1 then the entire pot goes to zero and the other player gets the dice.  
##
##ALGORITHM: I solved this problem as follows:
    # 1. Create a dice roll that returns a random number between 1-6
    # 2. Assign the first turn to the user
    # 3. Before each roll output score for both computer and user, whose turn it is and prompt the user to hit enter to continue
    # 4. Allow user to roll
    # 5. With each roll, output the die value and the amount to the pot
    # 6. If user rolls anything other than 1 that number is added to the pot and user can choose to roll again or hold(holding increments the player score by the pot amount, resets the pot and changes turns)
    # If user rolls a 1 then the pot is set to zero and the other player rolls
    # 7. The computer continues playing until the pot is 20 or more
    # 8. Declare a winner when the pot is greater or equal to 50.  Game also stops
    # 9. Upon conclusion, output score totals and winner
    # 10. Promt user if they want to play again
    # 11.Assign new game starting roll to not original roller(user)


import random

still_playing = True
user_turn = True
computer_turn = True
user_score = 0
computer_score = 0
pot = 0


# While the user is playing.
while still_playing:
    #Check to see if user or computer has won
    while user_score < 50 and computer_score < 50:
        #Output user and AI score
        print("Score" "    "   "You :", user_score,       "AI :",computer_score)
        

        # Check for users turn
        while user_turn == True:
            #Specify whose turn and ask user to continue by enter
            input("Your turn." "Hit enter to continue")

            die = random.randint(1, 6)
            if die == 1:
                pot = 0
                user_turn = False
                print("Die :", die, "Pot :", pot,   "BUST")
            if die != 1:
                print("Die :", die, "Pot :", pot, end = " ") 
                userChoice = input("(R)oll Again or (H)old?").upper()
                if userChoice in ["R", "H"]:
                    if userChoice == "H":
                        user_score = user_score + pot
                        user_turn = False
                    if userChoice == "R":
                        pot = pot + die
                        user_turn = True
                else:
                    continue
        # Check for computers turn
        while computer_turn == True:
            #restart the Pot
            pot = 0
            
            #Specify whose turn and ask user to continue by enter
            input("It's the computers turn." "Hit enter to continue")


            die = random.randint(1, 6)
            if die == 1:
                pot = 0
                print("Die :", die, "Pot :", pot,  "BUST")
                computer_turn = False
                user_turn = True
            if die != 1:
                if pot < 20:
                    pot = pot + die
                    computer_turn = True
                    print("Die :", die, "Pot :", pot)
                if pot > 20:
                    computer_score = computer_score + pot
                    computer_turn = False
                    user_turn = False
                    print("Die :", die, "Pot :", pot)


    else:
        if user_score >= 50:
            print("Congratulations You won")
            print("Score" "    "   "You :", user_score,       "AI :",computer_score)
        if computer_score >= 50: 
            print("You Lose")
            print("Score" "    "   "You :", user_score,       "AI :",computer_score)

    # Ask user if they want to play again
    userAnswer = input("Do you want to play PIG again? (Y)(YES)(N)(NO)").upper()
    if userAnswer in ["Y", "YES"]:
        still_playing = True
    elif userAnswer in ["N", "NO"]:
        still_playing = False
    else:
        continue


print("Thanks for playing")
        
    









