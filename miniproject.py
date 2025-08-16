import random as rd

choice = ['rock','paper','scissor']

def rock_paper_scissor():
    while True:
        print("Choices = [rock,paper,scissor]")
        user_input = input("Enter your choice: ").lower()
        computer_choice = rd.choice(choice)
        print('----------------------------')
        print("Computer_Choice: ",computer_choice)
        print("Your_Choice: ",user_input)

        if (computer_choice == user_input):
            print("The game is tie")
            print('\n')

        elif ( computer_choice=='paper' and user_input=='scissor')or\
             ( computer_choice=='scissor' and user_input=='rock' )or\
             ( computer_choice=='rock' and user_input=='paper' ):
            print("You Win")
            print('\n')

        
        else:
            print("You loose")
            print('\n')

rock_paper_scissor()  
