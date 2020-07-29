from random import randint

# Create a list of play options:
t= ["Stone" , "Paper" , "Scissor"]

# Assign a random play to the computer:
Computer = t [randint(0,2)]

# Set player to False:
Player = False

while Player == False:
# Set Player to True:9
    Player = input  ("Stone / Paper / Scissor?")
    print()
    if Player == Computer:
        print ("Tie!")
    elif Player == "Stone":
        if Computer == "Paper":
            print ("You lose!" , Computer , "covers" , Player)
        else:
            print ("You win!" , Player , "smashes" , Computer)
    elif Player == "Paper":
        if Computer == "Scissor":
            print ("You lose!" , Computer , "cuts" , Player)
        else:
            print ("You win!" , Player , "covers" , Computer)
    elif Player == "Scissor":
        if Computer == "Rock":
            print ("You lose!" , Computer , "smashes" , Player)
        else:
            print ("You Win!" , Computer , "cuts" , Player)
    else:
        print ("That's not a valid play,Please check your spelling")
    # Lets set the Player to False so loop continues.
    Player == False
    Computer = t [randint(0,2)]
