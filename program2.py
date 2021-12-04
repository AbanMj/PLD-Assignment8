print('    \nWelcome!!, Lets play a game: Guessing the Number')
import random

find= random.randint(0,100)

guess= float(input('\nGuess the number between 0-100 :   '))
while find != guess:
    
    if find>guess:
        print(' Greater than')
        guess= float(input('Guess again:   '))

    elif find< guess:
        print(' Less than')
        guess= float(input('Guess again:   '))
print(f"     \nWell done!! {find} is the number you should guess.")       
print("Congratulation! you Guess the number!")
