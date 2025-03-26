'''
gameboyUnadvanced.py
Mr.Price

Create a basic game selector and player. 

The selection screen should display this:

Select a game!
1. Roulette
2. Math Quiz
3. The Waiting Game
4. Quit

After this it should take an input for the number corresponding to the game. Be sure to error check that the number is indeed between 1 and 4.

If not, please output Invalid selection. Please pick a valid game number. and ask again.

The Selections should use functions to run the particular game. If you code the entire game within the if condition, it'll be points off.

 

roulette:

At the beginning seed the random number generator with the seed 10 with random.seed(10) This is for grading purposes.

Afterwards, generate a random number between 1 and 10. Prompt the player to guess by asking 

Guess a number between 1 and 10: 
If the guess right, print You Win! Otherwise print Wrong! Guess again! before prompting them for another input with the same message as above.
mathQuiz:
As before, seed the random number generator with the seed 10. Now generate 2 random numbers and ask the user
What is {firstNumber} + {secondNumber}? 
If they guess right, once again print You Win! and if they guess wrong print Wrong! Guess again! before repeating the same prompt as above. 
theWaitingGame:
Wait 5 seconds, then print You Win! then return.
Upon completion of any game, the game selection should repeat to prompt the user to select another game. This should only end if the user inputs 4 as their game selection in order to quit.

'''

#necessary libraries
import time
import random


#generates random number and compares user input to it
def roulette():

    random.seed(10)

    number=random.randint(1,10)

    guess=int(input("Guess a number between 1 and 10: "))


    while(guess!=number):
        print("Wrong! Guess again!")
        guess=int(input("Guess a number between 1 and 10: ")) 
    if(guess==number):
        print("You Win!")
        return 0
    


#generates 2 random numbers then challenges the user to find the sum of them
def mathQuiz():

    random.seed(10)
    random1 = random.randint(1,10)
    random2 = random.randint(1,10)
    number = random1 + random2

    guess = int(input(f"what is {random1} + {random2}? "))

    while(guess!=number):
        print("Wrong! Guess again!")
        guess=int(input(f"what is {random1} + {random2}? ")) 
    if(guess==number):
        print("You Win!")
        return 0
    

#waits for 5 seconds before printing you a win statement and returning 
def waitingGame():

    time.sleep(5)
    print("You Win!")
    return 0


#takes an input value, compares it to other numbers and then calls the function that the number corresponds to
input_value = 1

while(input_value!=4):
    print("Select a game!")
    print("1. Roulette")
    print("2. Math Quiz")
    print("3. The Waiting Game")
    print("4. Quit")

    input_value=int(input(""))

    while(input_value!=1 and input_value!=2 and input_value!=3 and input_value!=4):
        print("Invalid input, try again")
        print("Select a game!")
        print("1. Roulette")
        print("2. Math Quiz")
        print("3. The Waiting Game")
        print("4. Quit")

        input_value=int(input(""))
    else:
        if(input_value==1):
            roulette()
        
        if(input_value==2):
            mathQuiz()

        if(input_value==3):
            waitingGame()
