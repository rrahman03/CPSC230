#Raneem Rahman
#2/14/23
#rrahman@chapman.edu
#CPSC 230 section 05
#Assignment1_Basics-1

'''
The second program should be in a module, Celsius.py.  The program should prompt 
the user for the temperature in Celsius.  It should then convert this temperature into 
Fahrenheit and display the temperature in Fahrenheit. The conversion from Celsius 
to Fahrenheit is as follows: 𝑓𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡=𝑐𝑒𝑙𝑠𝑖𝑢𝑠(9/5)+32 
'''
celsius_temp = float(input('What is the temperature in celsius?')) #asking user for temperature in celsius
fahrenheit_temp = (celsius_temp * (9/5)+32) #conversion from celsius to fahrenheit 
print(fahrenheit_temp) #displays final temperature in fahrenheit

