#this is a guess the number game
#section 5
import random

print('Hellow, what is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 20')
secretNumber = random.randint(1,20)

for  guessesTaken in range(1, 7): #if guesses go through the range starting at 1 and ending at 7, the loop ends 
    print('Take a guess.')
    guess = int(input())

    if guess > secretNumber:
        print('your guess is too high')
    elif guess < secretNumber:
        print('your guess is too low')
    else:
        break #break out of the loop for a correct guess

#after loop breaks out 
if guess == secretNumber:
    print('good job '+ name +'! You guessed my number in ' + str(guessesTaken) + ' guesses.')
else:
    print('nope.  the number I was thinging of was '+ str(secretNumber))

    