import random

def lotteryf():
    
    tryagain= "yes"
    while tryagain[0]=='y': 
        first= random.randint(0,9)
        second=random.randint(0,9)
        third=random.randint(0,9)
        randoms= [first, second, third]

        numb1= int(input('\nEnter 1st number(0-9):    '))
        numb2= int(input('Enter 2nd number(0-9):    '))
        numb3= int(input('Enter 3rd number(0-9):    '))

        if numb1 in randoms and numb2 in randoms and numb3 in randoms :
            print("\nYou Win! Congratulation")
            print(f"The winning numbers are  {randoms}.")
            tryagain= input("Want to play again? (y or n):    ")      
        else:
            print ('\nYou lose')
            print(f"The winning numbers are  {randoms}.")
            tryagain= input("Try Again? (y or n):    ")      

lottery= lotteryf()
