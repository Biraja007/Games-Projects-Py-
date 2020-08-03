import random
Number= random.randint (1,10)

PlayerID= input ("Enter your name:")
NumberOfGuess = 0
print ("HEY! " + PlayerID + ".Guess a random number from 1 to 10: ")

while NumberOfGuess < 5:
    Guess= int ( input() )
    NumberOfGuess += 1
    if Guess < Number:
        print ("Your guess is too low.")
    if Guess > Number:
        print ("Your guess is too high.")
    if Guess == Number:
        break
if Guess == Number:
    print ("Your guess is correct in "  + str(NumberOfGuess) + " try")
else:
    print ("Out of try limit.Better luck next time!!!!!!!")
