#! /usr/bin/pythonw
##CS 101
##Program 1
##Malcolm Parrish
##mp2gb@mail.umkc.edu)
##
##PROBLEM: Write a Python program that gets the number of upper, lower, and corner cabinets from the user, then computes the cutting, sanding, finishing and total hours.  
##
##ALGORITHM: I solved this problem as follows:
##    1. Prompt the user for 
##    2. Find the 
##    1. Prompt the user for 

##
##ERROR HANDLING:
##    1. User is re-prompted until an int > 0 is entered.
##       Any other input is ignored.
##
##OTHER COMMENTS:
##     
##############################################################


uppercab_str = input("Enter the number of upper cabinets: ")
uppercab_int = int(uppercab_str)
lowercab_str = input("Enter the number of lower cabinets: ")
lowercab_int = int(lowercab_str)
cornercab_str = input("Enter the number of corner cabinets: ")
cornercab_int = int(cornercab_str)

total_cutting_hours_int = (uppercab_int * 1.2) + (lowercab_int * 1.5) + (cornercab_int * 1.9)
total_sanding_hours_int = (uppercab_int * 2.4) + (lowercab_int * 1.8) + (cornercab_int * 1.2)
total_finishing_hours_int = (uppercab_int * 3.4) + (lowercab_int * 2.5) + (cornercab_int * 1.5)
total_labor_hours_int = total_cutting_hours_int + total_sanding_hours_int + total_finishing_hours_int



print("Total cutting hours", total_cutting_hours_int)
print("Total sanding hours", total_sanding_hours_int)
print("Total finishing hours",  total_finishing_hours_int)
print("Total labor hours", total_labor_hours_int)




