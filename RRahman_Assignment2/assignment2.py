import random #importing random library

# this allows the user to enter the castle
# user is asked whether or not they want to enter
# depending on the user's answer, the game continues or the user exits
print('Would you like to enter the castle?') 
user = input('Yes or No? ') 
if user == 'Yes':
    print('Great!') 
if user == 'No': 
    print('Goodbye.')
    exit()

user = input('Would you like to exit the castle or open door One, Two, Three, Four, Five, or Six? ') # this line allows the user to decide which room they want to enter, or if they want to exit the game

# this loop allows user to open door one
# user can choose from a potion or cookie
# depending on the option the user chooses, they will die or move on in the game
while user == 'One': 
    my_var = random.randint(1,100) #this gives user a random chance of death
    if my_var >= 90:
        print('Sorry, you died. GAME OVER.')
        exit()
    print('Would you like to drink potion or eat the cookie? ') 
    user = input('Potion or Cookie: ') 
    while user == 'Potion': 
        print('Sorry, the potion was poison and you died. GAME OVER.') 
        break 
    while user == 'Cookie': 
        print('Congrats! There was a key in the cookie! Would you like to unlock the door in front of you? ')
        user = input('Yes or No? ') 
        while user == 'Yes':
            print('Congrats! You have unlocked the treasure! YOU WIN! GAME OVER.') 
            break
        while user == 'No':
            print('Sorry, you are stuck in this room forever. GAME OVER.') 
            break
while user == 'Exit': # this allows user to exit the game if they want
    print('Goodbye.')
    break

# this loop allows user to open door two 
# it has the same outcome as door one
# based on the choices the user makes in this loop, they will either die or move on in the game
while user == 'Two':
    my_var = random.randint(1,100) #this gives user a random chance of death
    if my_var >= 90:
        print('Sorry, you died. GAME OVER.')
        exit() 
    print('Would you like to drink potion or eat the cookie? ') 
    user = input('Potion or Cookie: ') 
    while user == 'Potion': 
        print('Sorry, the potion was poison and you died. GAME OVER.')
        break
    while user == 'Cookie': 
        print('Congrats! There was a key in the cookie! Would you like to unlock the door in front of you? ')
        user = input('Yes or No? ')
        while user == 'Yes':
            print('Congrats! You have unlocked the treasure. YOU WIN! GAME OVER.') 
            break
        while user == 'No':
            print('Sorry, you are stuck in this room forever. Game over.') 
            break
while user == 'Exit': #gives user the option to exit the game
    print('Goodbye.')
    break

# this loop allows user to open door three
# the user can choose from a room full of snakes or tigers
# depending on what choice they make, the outcome will be different: the user either wins the treasure or dies
while user == 'Three': 
    my_var = random.randint(1,100) #this gives user a random chance of death
    if my_var >= 90:
        print('Sorry, you died. GAME OVER.')
        exit()
    print('There are two doors in front of you. Would you like to enter room full of venomous snakes OR a room full of tigers who have not eaten in weeks? ')
    user = input('Snakes or Tigers: ') 
    while user == 'Snakes':
        print('Sorry! You were not strong enough to fight off the snakes. You died. GAME OVER.')
        break
    while user == 'Tigers':
        print('Congrats! Because the tigers have not eaten in weeks, they are dead. Would you like to go into room 5?' )
        user = input('Yes or No? ')
        while user == 'Yes':
            print('You are faced with two new doors, which one would you like to enter?')
            user = input('Room A or B? ')
            while user == 'A':
                print('Sorry, this door leads into the abyss. You have died. GAME OVER.')
                break
            while user == 'B':
                print('Congrats! This door was hiding the treasure you needed to find. YOU WIN! GAME OVER.')
                break
while user == 'Exit': # gives user the option to exit the game
    print('Goodbye.')
    break

# this loop allows user to open door four
# user is faced with a tiger and a bear; they have to choose which one they want to fight
# depending on the decision they make, they either die or move on in the game
while user == 'Four':
    my_var = random.randint(1,100) #this gives user a random chance of death
    if my_var >= 90:
        print('Sorry, you died. GAME OVER.')
        exit()
    print('You are faced with a bear and a tiger.')
    user = input('Which one would you like to fight? ')
    while user == 'Tiger':
        print('Sorry! You were not strong enough to fight off the tiger. You died. GAME OVER.')
        break
    while user == 'Bear':
        print('Lucky you! The bear was not strong enough to beat you. But now you are faced with two new doors, which one would you like to enter?')
        user = input('room A or B? ')
        while user == 'A':
            print('Sorry, this door leads into the abyss. You have died. GAME OVER.')
            break
        while user == 'B':
            print('Congrats! this door was the exit from the castle. YOU WIN! GAME OVER.')
            break
while user == 'Exit': # gives user the option to exit the game
    print('Goodbye.') 
    break

# this loop allows user to open door five
# the user is given the option of three slides to take
# depending on the slide they choose, the user either dies or continues on in the game
# i made door five a bigger loop than the previous ones, which means the user has more options
while user == 'Five':
    my_var = random.randint(1,100)
    if my_var >= 90:
        print('Sorry, you died. GAME OVER.')
        exit()
    print('You are faced with three slides in front of you, a red one, a green one, or a yellow one. Which one will you take?')
    user = input('Red, Green or Yellow? ')
    while user == 'Red':
        print('Sorry, this slide leads to a deep pit. You have died from falling. GAME OVER.')
        break 
    while user == 'Green':
        print('Sorry! This slide was lined with spikes and unfortunately you did not survive. GAME OVER.')
        break
    while user == 'Yellow':
        print('Congrats, you have survived the slide. Now, please choose which door you would like to open.')
        user = input ('door A or B? ')
        while user == 'a':
            print ('You are now faced with a riddle, which answer will you choose?')
            user = input('answer A, B or C? ')
            while user == 'a':
                print('Sorry, this was the wrong answer. Unfortunately you have lost. GAME OVER.')
                break
            while user == 'b':
                print('Correct! There is now a key in your hand, please unlock the door in front of you.')
                user = input('Did you unlock the door? ')
                while user == 'yes':
                    print('Congratulations! you have WON and found the treasure and fortune! GAME OVER!')
                    break 
            while user == 'c':
                print('Sorry, this was the wrong answer. Unfotunately you have lost. GAME OVER.')
                break
        while user == 'b':
            print('Sorry, this door leads to a pit of vicious snakes. You are now dead. GAME OVER.')
            break
while user == 'Exit': # gives user the option to exit the game
    print('Goodbye.')
    break

# this loop allows user to enter door six
# the user is faced with two doors
# depending on which door the user takes, there will be different choices to make
# based on these choices, the user either dies or continues on in the game
# i made door six the biggest loop compared to the previous ones, which means the user has more options
while user == 'Six':
    my_var = random.randint(1,100) #this gives user a random chance of death
    if my_var >= 90:
        print('Sorry, you died. GAME OVER.')
        exit()
    print('You are faced with two doors. Which one will you pick?') 
    user = input('Door A or B? ')
    while user == 'A':
        print('There are now two more doors in front of you. Please choose one.')
        user = input('Door One or Two? ') 
        while user == 'One':
            print('You have entered a maze. Will you be turning right or left?')
            user = input('Right or Left? ') 
            while user == 'Right':
                print('You have reached a dead end. Would you like to turn left or go back?')
                user = input('Turn left or go back? ') 
                while user == 'Turn left':
                    print('You have reached door 2. would you like to open it?')
                    user = input('Yes or No? ')
                    while user == 'Yes':
                        print('Would you like to drink potion or eat the cookie? ')
                        user = input('Potion or Cookie: ') 
                        while user == 'Potion':
                            print('Sorry, the potion was poison and you died. GAME OVER.')
                            break
                        while user  == 'Cookie':
                            print('Congrats! There was a key in the cookie! Would you like to unlock the door in front of you? ') 
                            break
                            user = input('Yes or No? ')  
                            while user == 'Yes': 
                                print('Congrats! You have unlocked the room holding the treasure! YOU WIN! GAME OVER.')
                                break
                    while user == 'No':
                     print('Sorry, you are stuck in this room forever. GAME OVER.')
                     break       
                while user == 'Go back': 
                    print('Sorry, you have run out of time in the maze. GAME OVER.')
                    break
                while user == 'Turn left':
                    print('You have reached door 4, would you like to enter?')
                    user = input('Yes or No? ')
                    while user == 'Yes':
                        print('You have been faced with a Bear and a Tiger.')
                        user = input('Which one would you like to fight? ')
                        while user == 'Tiger':
                            print('Sorry! You were not strong enough to fight off the tiger. You died. GAME OVER.')
                            break 
                        while user == 'Bear':
                            print('Lucky you! The bear was not strong enough to beat you. But now you are faced with two new doors, which one would you like to enter?')  
                            user = input('room A or B? ')
                            while user == 'A':
                                print('Sorry, this door leads into the abyss. You have died. GAME OVER.')
                                break
                            while user == 'B':
                                print('Congrats! You have unlocked the room holding the treasure! YOU WIN! GAME OVER.')
                    while user == 'No':
                        print('Sorry you have run out of time in the maze. Game over.')
                        break
    while user == 'B':
        print('You now have an envelope in front of you. Please open it.')
        user = input('Have you opened the envelope? ')
        while user == 'Yes':
            print('You are now faced with a riddle, which answer will you choose?')
            user = input('answer A, B or C? ')
            while user == 'A':
                print('Sorry, this was the wrong answer. Unfotunately you have lost. GAME OVER.')
                break
            while user == 'B':
                print('Correct! There is now a key in your hand, Please unlock the door in front of you.')
                user = input('say the word UNLOCK to open the door: ')
                while user == 'UNLOCK':
                    print('Congratulations! You have WON and found the treasure and fortune! GAME OVER!')
                    break
            while user == 'C': 
                print('Sorry, this was the wrong answer. Unfortunately you have lost. GAME OVER.')
                break
while user == 'Exit':
    print('Goodbye.')
    break
