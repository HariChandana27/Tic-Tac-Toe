from tkinter import *
from tkinter import messagebox
from functools import partial
import random 

#tic tac toe board
board=[['   ' for j in range(3)] for i in range(3)]
btn = [['   ' for j in range(3)] for i in range(3)]

def check_win():
    global board
    win = False
    #checking for win via row
    if(board[0][0]==board[0][1]==board[0][2] and board[0][0]!='   '):
        win = True
    if(board[1][0]==board[1][1]==board[1][2] and board[1][0]!='   '):
        win = True
    if(board[2][0]==board[2][1]==board[2][2] and board[2][0]!='   '):
        win = True
    #via column
    if(board[0][0]==board[1][0]==board[2][0] and board[0][0]!='   '):
        win = True
    if(board[0][1]==board[1][1]==board[2][1] and board[0][1]!='   '):
        win = True
    if(board[0][2]==board[1][2]==board[2][2] and board[0][2]!='   '):
        win = True
    #via diagonal
    if(board[0][0]==board[1][1]==board[2][2] and board[0][0]!='   '):
        win = True
    if(board[0][2]==board[1][1]==board[2][0] and board[0][2]!='   '):
        win = True
    return win

def check_tie():
    #checking for a tie
    global board
    count = 0
    for i in range(3):
        for j in range(3):
            if(board[i][j]=='   '):
                count +=1
    if(count==0):
        return True
    else:
        return False

def change_player(): 
    global turn
    #changind the player in the case of multiple player
    if (turn=='A'):
        turn = 'B'
    elif(turn=='B'):
        turn = 'A'
    #in the case of single player
    elif(turn=='AI'):
        turn = 'Player'
    else:
        turn = 'AI'

#utility function to calculate utitlity/score for the minimax algorithm
def calc_utility():
    #returns 1 if AI wins
    #returns -1 if player wins
    #via row
    if(board[0][0] == board[0][1] == board[0][2]):
        if(board[0][0] == 'X'):
            return 1
        if(board[0][0] == 'O'):
            return -1
    if(board[1][0] == board[1][1] == board[1][2]):
        if(board[1][0] == 'X'):
            return 1
        if(board[1][0] == 'O'):
            return -1
    if(board[2][0] == board[2][1] == board[2][2]):
        if(board[2][0] == 'X'):
            return 1
        if(board[2][0] == 'O'):
            return -1
    #via column
    if(board[0][0] == board[1][0] == board[2][0]):
        if(board[0][0] == 'X'):
            return 1
        if(board[0][0] == 'O'):
            return -1
    if(board[0][1] == board[1][1] == board[2][1]):
        if(board[0][1] == 'X'):
            return 1
        if(board[0][1] == 'O'):
            return -1
    if(board[0][2] == board[1][2] == board[2][2]):
        if(board[0][2] == 'X'):
            return 1
        if(board[0][2] == 'O'):
            return -1
    #via diagonal
    if(board[0][0] == board[1][1] == board[2][2]):
        if(board[0][0] == 'X'):
            return 1
        if(board[0][0] == 'O'):
            return -1
    if(board[0][2] == board[1][1] == board[2][0]):
        if(board[0][2] == 'X'):
            return 1
        if(board[0][2] == 'O'):
            return -1
    #returns 0 if there is no win by AI or the player
    return 0

#using minimax algorithm for AI's (smart) play
def minimax(AITurn):
    global max_val,min_val
    #base case - returns utility for terminal states or in the case of a tie 
    if(calc_utility() ==-1 or calc_utility() == 1):
        return calc_utility()
    if(check_tie()):
        return 0
    #recursive case - maximizer turn
    if(AITurn):
        max_val = -100 
        for i in range(3):
            for j in range(3):
                if(board[i][j]=='   '):
                    board[i][j] = 'X'
                    temp2 = minimax(False)
                    if(max_val < temp2 ):
                        max_val = temp2
                    board[i][j] = '   '
        return max_val
    #minimizer turn
    else:
        min_val = +100 
        for i in range(3):
            for j in range(3):
                if(board[i][j]=='   '):
                    board[i][j] = 'O'
                    temp3 = minimax(True)
                    if(min_val > temp3):
                        min_val = temp3
                    board[i][j] = '   '
        return min_val

#the first move in single player is always by AI and is random
def random_move():
    a,b = random.randint(0,2),random.randint(0,2)
    board[a][b] = 'X'
    return(a,b)

#the rest of the moves by AI are logical
#calls minimax function to decide the best next move
def logical_move(main,lbl):
    global board
    best = -100
    for i in range(3):
        for j in range(3):
            if(board[i][j]=='   '):
                board[i][j] = 'X'
                temp = minimax(False)
                if(best<temp):
                    best = temp
                    m,n = i,j 
                board[i][j] ='   '
    board[m][n] = 'X'
    btn[m][n].config(text=board[m][n],state=DISABLED,bg='gray63',font=("Geneva", "9", "bold"))
    #ends the game if there is a win
    if(check_win()):
        win_box = messagebox.showinfo("Win",f"{turn} won the match!")
        board=[['   ' for j in range(3)] for i in range(3)]
        main.destroy()
    #ends the game if there is a tie
    elif(check_tie()):
        tie_box = messagebox.showinfo("Tie","No one won this match")
        board=[['   ' for j in range(3)] for i in range(3)]
        main.destroy()
    else:
        change_player()

#updates the selection of the player in the case of single player 
def update_mp(main,lbl,i,j):
    global turn,board
    lbl['text']= "Your move"
    if(board[i][j]=='   '):
        board[i][j] = 'O'
        btn[i][j].config(state=DISABLED,bg='hotpink3',font=("Geneva", "9", "bold"))
        btn[i][j].config(text=board[i][j])
        if(check_win()):
            win_box = messagebox.showinfo("Win",f"{turn} won the match!")
            board=[['   ' for j in range(3)] for i in range(3)]
            main.destroy()
        elif(check_tie()):
            tie_box = messagebox.showinfo("Tie","No one won this match")
            board=[['   ' for j in range(3)] for i in range(3)]
            main.destroy()
        else:
            logical_move(main,lbl)

#updates the selection of the players in the case of multiple players
def update_sp(main,lbl,i,j):
    global turn,board
    if(board[i][j]=='   '):
        if(turn=='A'):
            board[i][j] = 'X'
            btn[i][j].config(state=DISABLED,bg='gray63',font=("Geneva", "9", "bold"))
        else:
            board[i][j] = 'O'
            btn[i][j].config(state=DISABLED,bg='hotpink3',font=("Geneva", "9", "bold"))
        btn[i][j].config(text=board[i][j])
        if(check_win()):
            win_box = messagebox.showinfo("Win",f"{turn} won the match!")
            board=[['   ' for j in range(3)] for i in range(3)]
            main.destroy()
        elif(check_tie()):
            tie_box = messagebox.showinfo("Tie","No one won this match")
            board=[['   ' for j in range(3)] for i in range(3)]
            main.destroy()
        else:
            change_player()
            lbl['text']= f"It's {turn}'s turn"

#the main window of the game 
def window():
    main = Tk()
    lbl = Label(main,text=f"It's {turn}'s turn",width=6,height=2,bg='OliveDrab2')
    lbl.grid(row=0,column=1,sticky='ew')
    return(main,lbl)

#creating layout and updating the selection in the case of single player
def single_player(): 
    global turn
    turn='AI'
    main,lbl = window()
    lbl['text']= "Your move"
    #first move is random by AI
    a,b = random_move()
    change_player()
    for i in range(3):
        btn.append(i)
        btn[i]=[]
        for j in range(3):
            btn[i].append(j)
            update_text = partial(update_mp,main,lbl,i,j)
            btn[i][j] = Button(main,text=board[i][j],command=update_text,width=10,height=5)
            btn[i][j].grid(row=i+2,column=j)
    btn[a][b].config(state=DISABLED,bg='gray63',font=("Geneva", "9", "bold"))
    main.mainloop()

#creating layout and updating the selection in the case of multiple player
def multiple_player(): 
    global turn
    turn='A'
    main,lbl = window()
    for i in range(3):
        btn.append(i)
        btn[i]=[]
        for j in range(3):
            btn[i].append(j)
            update_text = partial(update_sp,main,lbl,i,j)
            btn[i][j] = Button(main,text=board[i][j],command=update_text,width=10,height=5)
            btn[i][j].grid(row=i+2,column=j)
    main.mainloop()

#the menu board
def menu_board():
    menu.title("Tic Tac Toe")
    menu_lbl = Label(menu,text="Let's play Tic Tac Toe",width=20,height=2,bg='khaki3')
    menu_lbl.grid(row=0,column=0,sticky='ewns')
    sp_btn = Button(menu,text = 'Single Player',command = single_player,width=15,height=2,bg='light coral')
    sp_btn.grid()
    mp_btn = Button(menu,text = 'Multiple Player',command = multiple_player,width=15,height=2,bg='light coral')
    mp_btn.grid()
    menu.mainloop()

#main funtion
menu = Tk()
menu_board()




