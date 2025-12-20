board=[['' for i in range(3)] for i in range(3)]
player1="X"
player2="O"
count = 2

    
def printboard(board):
    for row in board:
        for element in row:
            print(element ,end =" | " )
        print('\n')
    

def play(selected_player):
    print(f"{selected_player}'s Turn") 
    print(f"Choose where to play \n 1,1 | 1,2 | 1,3 \n 2,1 | 2,2 | 2,3 \n 3,1 | 3,2 | 3,3\n")
    update(list(input("\nEnter the position as given ")),selected_player)
    
    
def update(a,b):
    global count
    global player1
    global player2
    indx1=int(a[0])-1
    indx2=int(a[2])-1
    if (Check(indx1,indx2)):
        board[indx1][indx2]= b
        count +=1 
        print(f"\nUpdated Sucessfully at  {a[0]},{a[2]}\n")
        printboard(board)
    
def Check(a,b):
    if board[a][b] =="":
        return True
    else:
        print("\nPlace is occupied choose another place\n")
        return False

def player_turn():
    global count
    if count % 2 == 0:
        return player1
    else :
        return player2
def check_win(player):
    global board
    coln = True
    row = True
    
    for i in range(3):
        for j in range(3):
            if(board[i][j]!=player):
                row = False

            if(board[j][i]!=player):
                coln =False
           

        
        if(coln):
            print(f"{player} has won")
            return True
        
        
        if(row):
            print(f"{player} has won")
            return True
        if(board[0][0]==board[1][1]==board[2][2]==player):
            print(f"{player} has won")
            return True
        if(board[0][2]==board[1][1]==board[2][0]==player):
            print(f"{player} has won")
            return True
        
        
    
    
        
printboard(board)
while True:
        play(player_turn())
        if(check_win(player1)):
            break
        if(check_win(player2)):
            break
