# function returns the names in pig Latin
def word_to_pig(name): 
	consonantcheck = True
	consonant=""
	# defines vowels
	vowels = ["a","e","i","o","u","y","A","E","I","O","U","Y"] 
	# loop that checks for consonants
	while consonantcheck:
		for letter in name:
			if letter not in vowels:
				consonant += letter
			else:
				consonantcheck=False
				break	
		consonantcheck=False
      # checks the length of existing consonant
	if (len(consonant)==0):
		# checks if first input letter is uppercase
		if name[0].isupper():
			output = name.lower().capitalize()+"yay"
		else:
			output = name.lower()+"yay"
	# if we have consonants, we need to remove them from the start
      # append them to the end and append ay
	else:
		if name[0].isupper():
			output = name.removeprefix(consonant)+consonant+"ay" 
			output = output[0].upper() + output.lower()[1:]
		else:
			output = name.removeprefix(consonant)+consonant+"ay"
			output = output.lower()
	return output

# takes 2 input parameters, first_name and last_name, and will use your word_to_pig function to do the translation to avoid duplicating code.	
def name_to_pig(firstname, lastname):
	return (word_to_pig(firstname)+ " " + word_to_pig(lastname))


uname = input("Enter your firstname and lastname: ")

# taking the input and splitting it into first name and last name
name = uname.split(); 
# check if the length of the input is exactly two, and there are no non alpha characters
# keeps asking until condition is met
while (len(name)!=2 or name[0].isalpha() == False or name[1].isalpha() == False ): 
	uname = input("Please enter only a firstname and lastname: ") # asking for user input
	name = uname.split() 


# printing out the ouput from name_to_pig functions, calling the function with the first name and last name
print (name_to_pig(name[0], name[1])) 


