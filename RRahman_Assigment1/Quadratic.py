#Raneem Rahman
#2/14/23
#rrahman@chapman.edu
#CPSC 230 section 05
#Assignment1_Basics-1

'''
The third program should be in a module, Quadratic.py. The program should prompt 
the user for the coefficients a, b, c of a quadratic function.  The program should then 
calculate and display the roots of the function using the quadratic formula.  (Hint: 
Use the math module to calculate a square root). For now, only use values that will 
return a positive discriminate, test a = -1, b = 2, c = 3, you should get x = -1 and x = 3 
for answers. 
'''

import math
a = float(input('what is coefficient a?')) #asking user for first coefficient
b = float(input('what is coefficient b?')) #asking user for second coefficient
c = float(input('what is coefficient c?')) #asking user for third coefficient 1

d = (b ** 2 - 4 * a * c)
if d < 0:
    print('Cannot solve, is negative.') #tells user there cannot be a negative discriminant
elif d == 0:
    a_1 = (-b + math.sqrt(d))/(2 * a) #quadratic formula
    print ('x: ', a_1) #gives the user the x value
else:
    answer_1 = (-b + math.sqrt(d))/(2 * a) #quadratic formula
    answer_2 = (-b - math.sqrt(d))/(2 * a) #quadratic formula

    print('value_1:' , answer_1) #gives the user the first value
    print('value_2:' , answer_2) #gives the user the second value
