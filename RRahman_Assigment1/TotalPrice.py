#Raneem Rahman
#2/14/23
#rrahman@chapman.edu
#CPSC 230 section 05
#Assignment1_Basics-1

'''
The first program should be in a module, TotalPrice.py. The program should find the 
# total price of an item given the price and sales tax. The program should prompt the 
user for the purchase price of an item and the sales tax rate, it should display the 
total price of the item.  The user should be able to enter values such as 10.25 for 
price and 7.5 for sales tax rate. Think about how you are going to calculate total 
price, check to make sure it makes sense. 
'''

purchase_price = float(input('what is the price of the item?')) #asking the user to input the price of item
sales_tax = float(input('what is the sales tax?')) #asking the user to imput the sales tax

total_price = (((sales_tax/100) * purchase_price) + purchase_price) #adding the sales tax onto the price of the item
print(total_price) #gives the user the final price