
def lotteryf():
    tryagain= "y"
    while tryagain[0]=='y':
        
        def numbinput():
            numb1= int(input('\nEnter 1st number(0-9):    '))
            numb2= int(input('Enter 2nd number(0-9):    '))
            numb3= int(input('Enter 3rd number(0-9):    '))
            return numb1, numb2,numb3
        numbers= numbinput()
          
        import random
        for forwin_numb in range(1):
            first= random.randint(0,9)
            second=random.randint(0,9)
            third=random.randint(0,9)
        print(f"\nThe winning numbers are  {first},  {second},  {third}.")
            
        if numbers==forwin_numb:
            print("You Win! Congratulation")
        else:
            print ('You loss')
            tryagain= input("Try Again (y or n):    ")      

lottery= lotteryf()
