import random
import math

#Taking inputs
a = int(input("Enter the start number for the range:"))
b = int(input("Enter the highest number for the range:"))

#generating random number between a and b
x = random.randint(a,b)
print("\n You have only ",
      round (math.log(b - a + 1, 2)),
      "chances to guess the integer!\n")

#initializing number of counts
count = 0

'''for calculation of minimum number of
guesses depends upon range'''

while count<math.log(b - a + 1, 2):
    count += 1

    #taking guessing number as input
    guess = int (input("Guess a number:"))

    #condition testing
    if x == guess:
        print ("Congratulations, this is the correct number.You did it in",count,"try/tries")
        break
    elif x>guess:
        print ("You guessed too small!")
    elif x<guess:
        print ("You guessed too high!")

#If guessing is more than the number of counts. 
#then gives this output. 

if count>= math.log(b - a + 1, 2):
    print ("\n The number is %d" %x)
    print ("\n Better luck next time!")
