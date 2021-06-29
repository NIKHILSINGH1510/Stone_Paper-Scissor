from tkinter import *
from PIL import Image, ImageTk
from random import randint


window = Tk()
window.title("Stone Paper Scissor")
window.configure(background = "black")

image_rock = ImageTk.PhotoImage(Image.open("stone.png"))
image_paper = ImageTk.PhotoImage(Image.open("paper.png"))
image_scissor = ImageTk.PhotoImage(Image.open("scissors.png"))

label_player= Label(window, image= image_scissor)
label_computer=Label(window, image=image_scissor)

label_computer.grid(row=1, column =0)
label_player.grid(row=1, column =4)

computer_score = Label(window,text=0, font=("arial",60,"bold"),fg="red")

player_score = Label(window,text=0, font=("arial",60,"bold"),fg="red")
computer_score.grid(row=1,column=1)
player_score.grid(row=1,column=3)

player_indicator= Label(window,font=("arial",40,"bold"),text="YOU",bg="orange",fg="blue")
computer_indicator= Label(window,font=("arial",40,"bold"),text="COMPUTER",bg="orange",fg="blue")

computer_indicator.grid(row=0,column=1)
player_indicator.grid(row=0,column=3)

def msg_updation(a):
    final_message['text']=a

def comp_update():
    final = int(computer_score['text'])
    final += 1
    computer_score['text']= str(final)

def player_update():
    final = int(player_score['text'])
    final +=1
    player_score['text']= str(final)

def winner(p,c):
    if p==c:
        msg_updation("It's a tie")
    elif p=="rock":
        if c == "paper":
            msg_updation("Computer wins!!")
            comp_update()
        else:
            msg_updation("You win!!")
            player_update()
    elif p=="paper":
        if c == "scissor":
            msg_updation("Computer wins!!")
            comp_update()
        else:
            msg_updation("You win!!")
            player_update()
    elif p=="scissor":
        if c=="rock":
            msg_updation("Computer wins!!")
            comp_update()
        else:
            msg_updation("You win!!")
            player_update()
    else:
        pass
to_select = ["rock", "paper","scissor"]

def choice_update(a):
    choice_computer = to_select[randint(0,2)]
    if choice_computer == "rock":
            label_computer.configure(image = image_rock)
    elif choice_computer == "paper":
                label_computer.configure(image = image_paper)
    else:
                label_computer.configure(image = image_scissor)

    if a=="rock":
            label_player.configure(image = image_rock)
    elif a=="paper":
            label_player.configure(image = image_paper)
    else:
            label_player.configure(image = image_scissor)
        
    winner(a,choice_computer)

             
        

final_message = Label(window,font=("arial",20,"bold"),bg="red",fg="white")
final_message.grid(row=3,column =2)

button_rock= Button(window, width=16, height = 3, text="ROCK",font =("arial",20,"bold"),bg="yellow",fg="red",command=lambda:choice_update("rock")).grid(row=2,column=1)
button_paper= Button(window, width=16, height = 3, text="PAPER",font =("arial",20,"bold"),bg="yellow",fg="red",command=lambda:choice_update("paper")).grid(row=2,column=2)
button_scissor= Button(window, width=16, height = 3, text="SCISSOR",font =("arial",20,"bold"),bg="yellow",fg="red",command=lambda:choice_update("scissor")).grid(row=2,column=3)

window.mainloop()

