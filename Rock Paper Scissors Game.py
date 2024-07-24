import random
l=["Rock","Paper","Scissor"]
"""
rock v/s paper = paper wins
rock v/s scissor = rock wins
scissor v/s paper = scissor wins
"""
while True:
    uscore=0
    Cscore=0
    u=int(input('''
1 = Start Game
2 = Exit'''))
    if u==1:
        pass
        for a in range(1,6):
            uinput=int(input('''
1 = Rock
2 = Paper
3 = Scissor'''))
        
            if uinput==1:
                uchoice="Rock"
            elif uinput==2:
                uchoice="Paper"
            elif uinput==3:
                uchoice="Scissor"
            else:
                print("Invalid input")
                print("Your Score =",uscore)
                print("Computer's Score =",Cscore)
                break
            Cchoice=random.choice(l)
            if uchoice==Cchoice:
                print("Your Choice",uchoice)
                print("Computer's Choice",Cchoice)
                print("Your Score =",uscore)
                print("Computer's Score =",Cscore)
            elif (uchoice=="Rock" and Cchoice=="Scissor") or (uchoice=="Paper" and Cchoice=="Rock") or (uchoice=="Scissor" and Cchoice=="Paper"):
                print("Your Choice",uchoice)
                print("Computer's Choice",Cchoice)
                uscore=uscore+1
                print("Your Score =",uscore)
                print("Computer's Score =",Cscore)
                
            else:
                print("Your Choice",uchoice)
                print("Computer's Choice",Cchoice)
                Cscore=Cscore+1
                print("Your Score =",uscore)
                print("Computer's Score =",Cscore)
                
        if uscore==Cscore:
            print("THE GAME DRAWS")
        elif uscore>Cscore:
             print("YOU WIN THE GAME")
        else:
            print("COMPUTER WINS THE GAME")
    elif u==2:
        break
    else:
        print("Invalid input")
        break
            
    
