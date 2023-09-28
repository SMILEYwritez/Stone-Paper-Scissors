import random 
import sys
ai=0
user=0
def end():
    print("It was a fun game. Sad to see you go")
    sys.exit(0)
def restart():
    r=int(input("If u want to play again press 1 \nor press any key to exit \n"))
    if r==1:
        pass
        main()
    else:
        pass 
        end()
def win():
    global ai,user
    ai+=1
    print("I won")
    print("Score \nAI :-",ai,"\nYOU:-",user)
    restart()
def lose():
    global ai,user
    user+=1
    print("Aagh I lost")
    print("Score \nAI :-",ai,"\nYOU:-",user)
    restart()
def draw():
    global ai,user
    print("Its a draw :(")
    print("Score \nAI :-",ai,"\nYOU:-",user)
    restart()
def main():
    choise=["Rock","Paper","Scissors"]
    computerchoise=random.choice(choise)
    u_choice=int(input("Input \n1 for Rock \n2 for Paper \n3 for Scissors \n"))
    if u_choice==1:
        a="Rock"
    if u_choice==2:
        a="Paper"
    if u_choice==3:
        a="Scissors"
    if u_choice==1 and computerchoise=="Rock":
        print("YOU:-",a,"\nAI :-",computerchoise)
        draw()
    elif u_choice==2 and computerchoise=="Rock":
        print("YOU:-",a,"\nAI :-",computerchoise)
        lose()
    elif u_choice==3 and computerchoise=="Rock":
        print("YOU:-",a,"\nAI :-",computerchoise)
        win()
    elif u_choice==1 and computerchoise=="Paper":
        print("YOU:-",a,"\nAI :-",computerchoise)
        win()
    elif u_choice==2 and computerchoise=="Paper":
        print("YOU:-",a,"\nAI :-",computerchoise)
        draw()
    elif u_choice==3 and computerchoise=="Paper":
        print("YOU:-",a,"\nAI :-",computerchoise)
        lose()
    elif u_choice==1 and computerchoise=="Scissors":
        print("YOU:-",a,"\nAI :-",computerchoise)
        lose()
    if u_choice==2 and computerchoise=="Scissors":
        print("YOU:-",a,"\nAI :-",computerchoise)
        win()
    elif u_choice==3 and computerchoise=="Scissors":
        print("YOU:-",a,"\nAI :-",computerchoise)
        draw()
    else:
        print("YOU DUMB IDIOT")
main()