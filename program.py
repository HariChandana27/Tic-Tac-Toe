from tkinter import *
from tkinter import messagebox
from functools import partial

#creating the main window
main = Tk()

global btn, board

#creating an empty tic tac toe board
board=[['   ','   ','   '],['   ','   ','   '],['   ','   ','   ']]
btn = []

turn='A'

#creating the label to inform the players about their turns
lbl = Label(main,text=f"It's {turn}'s turn",width=6,height=2,bg='lavender')
lbl.grid(row=0,column=1,sticky='ew')

#function to check for player's win
def check_win():
    #checking for win via rows
    win = False
    if(board[0][0]==board[0][1]==board[0][2] and board[0][0]!='   '):
        win = True
    if(board[1][0]==board[1][1]==board[1][2] and board[1][0]!='   '):
        win = True
    if(board[2][0]==board[2][1]==board[2][2] and board[2][0]!='   '):
        win = True
    #checking for win via columns
    if(board[0][0]==board[1][0]==board[2][0] and board[0][0]!='   '):
        win = True
    if(board[0][1]==board[1][1]==board[2][1] and board[0][1]!='   '):
        win = True
    if(board[0][2]==board[1][2]==board[2][2] and board[0][2]!='   '):
        win = True
    #checking for win via diagnals
    if(board[0][0]==board[1][1]==board[2][2] and board[0][0]!='   '):
        win = True
    if(board[0][2]==board[1][1]==board[2][0] and board[0][2]!='   '):
        win = True
    if(win==True):
        win_box = messagebox.showinfo("Win",f"{turn} won the match!")
    return win

#function to check for a tie
def check_tie(): 
    count = 0
    for i in range(3):
        for j in range(3):
            if(board[i][j]=='   '):
                count +=1
    if(count==0):
        tie_box = messagebox.showinfo("Tie","No one won this match")
        return True
    else:
        return False

def change_player(): 
    global turn
    if (turn=='A'):
        turn = 'B'
    else:
        turn = 'A'

#updating the choice of the player in the tic tac toe board    
def update(i,j):
    global turn
    if(board[i][j]=='   '):
        if(turn=='A'):
            board[i][j] = 'X'
            btn[i][j].config(state=DISABLED,bg='gray63',font=("Geneva", "9", "bold"))
        else:
            board[i][j] = 'O'
            btn[i][j].config(state=DISABLED,bg='hotpink3',font=("Geneva", "9", "bold"))
        btn[i][j].config(text=board[i][j])
        #terminating the window if there is a win or tie
        if(check_win()==True or check_tie()==True):
            main.destroy()
        else:
            change_player()
            lbl['text']= f"It's {turn}'s turn"


def create_board():
    #creating the GUI based Tic Tac Toe board
    for i in range(3):
        btn.append(i)
        btn[i]=[]
        for j in range(3):
            btn[i].append(j)
            update_text = partial(update,i,j)
            btn[i][j] = Button(main,text=board[i][j],command=update_text,width=10,height=5)
            btn[i][j].grid(row=i+2,column=j)
    main.mainloop()
    
#main funtion
create_board()


