from random import randint
t=["rock","paper","scissor"]
computer=t[randint(0,2)]
player=False
while player==False:
    player=input("rock,paper,scissor ?")
    if player==computer:
        print("Tie")
    elif player=="rock":
        if computer=="paper":
            print("you lose")
        else:
            print("you win this game")
    elif player=="paper":
        if computer=="scissor":
            print("you lose")
        else:
            print("you win this game")
    elif player=="scissor":
        if computer=="rock":
            print("you lose")
        else:
            print("you win this game")
    else:
        print(" this is wrong input ")
    player==False
    computer=t[randint(0,2)]


