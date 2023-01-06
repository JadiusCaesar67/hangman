from time import *
from threading import Thread
counter = 5
timer = 32
print(f"""Welcome to Jade's GUESS THE WORD GAME!  In this series of guess the word game: 
         You should be able to guess one of the names of famous conquerors in the old times, from ancient times to industrial period.
     You can attempt to guess by up to {counter} times only and has only up to {timer - 2} seconds to guess the name. \n""")
sleep(2)
print("Note: Enter the first name or the last name only and the first letter should be capitalized... Good luck! \n")
sleep(3)
input('Press enter to start the game \n')
def countdown():
    global timer

    for x in range(timer):
        #timer -= 1
        print(timer, end="\r")
        sleep(1)       
countdown_thread = Thread(target = countdown)
countdown_thread.start()

word = ['Alexander', 'Julius', 'Caesar', 'Augustus', 'Charlemagne', 'Genghis', 'Khan', 'Napoleon', 'Bonaparte']
guess = ''
enter = ''
count = 0
limit = 5
out_of_limit = False
while guess != word and timer > 0 and not out_of_limit:
    if count < limit:
        if count != 0:
            counter -= 1
            print(f'\nYou only have {counter} guesses left.')
        guess = str(input("Type in the name: "))
        if guess in word:
            print(f'{guess.capitalize()} is correct.\n Conratulations you WIN!')
            break
        if guess == enter:
            print('\nPlease enter a name')
        elif guess.capitalize() in word:
            print('\nPlease capitalize the first letter!')
        else:
            print('\nWRONG!')
        count += 1
    else:
        out_of_limit = True
        print('Out of guesses. You LOSE!') 
        break
    if timer == 0:
        print("\n Time is up!!!")
        break
#else:
#    print("Game is over already, please restart the game")