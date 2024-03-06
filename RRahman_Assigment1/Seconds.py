#Raneem Rahman
#2/14/23
#rrahman@chapman.edu
#CPSC 230 section 05
#Assignment1_Basics-1

'''
The fourth program should be in a module, Seconds.py.  A day has 86,400 seconds 
(24*60*60). The program should prompt the user for a number in range 1 to 86,400 
and output the current time as hours, minutes, and seconds with a 24-hour clock. 
For example: 70,000 seconds is 19 hours, 26 minutes, and 40 seconds. (Hint: Think 
about your quotient integer and quotient remainder operations.) 
'''

import math #for mathematical functions
number = int(input('give a number between 1 and 86,400:')) #allows user to insert value
hours = number // 3600 #division
number = number % 3600 #finds remainder
minutes = number // 60 #division
number = number % 60 #finds remainder

print('hours:' , hours, 'minutes:' , minutes , 'seconds:' , number,) #gives user the final time