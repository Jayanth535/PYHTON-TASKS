from random import randrange
 
def display_board(board):
    print(' +-------+-------+-------+\n','|       |       |       |\n',
          '|   ' +board[0][0]+    '   |   ' +board[0][1] +   '   |   ' +board[0][2] +   '   |\n','|       |       |       |',)
    print(' +-------+-------+-------+\n','|       |       |       |\n',
          '|   ' +board[1][0]+    '   |   ' +board[1][1] +   '   |   ' +board[1][2] +   '   |\n','|       |       |       |',)
    print(' +-------+-------+-------+\n','|       |       |       |\n',
          '|   ' +board[2][0]+    '   |   ' +board[2][1] +   '   |   ' +board[2][2] +   '   |\n','|       |       |       |',)
    print(' +-------+-------+-------+')
board=[['1','2','3'],['4','X','6'],['7','8','9']]
display_board(board)

def enter_move(board):
    choice=input("Enter your move: ")
    for row in range(3):
        for col in range(3):
            if board[row][col]==choice:
                board[row][col]="O"
enter_move(board)  
display_board(board)   
        
def make_list_of_free_fields(board):
    global free_fields
    free_fields=[]
    for row in range(3):
        for col in range(3):
            if board[row][col] !='O' and  board[row][col]!='X':
                free_fields.append([[row],[col]])
make_list_of_free_fields(board)
def victory_for(board, sign):
        #for rows

    if board[0][0]==sign and  board[0][1]==sign and   board[0][2]==sign:
        print(sign," is the winner ")
    if board[1][0]==sign and  board[1][1]==sign and   board[1][2]==sign:
        print(sign," is the winner ")
    if board[2][0]==sign and  board[2][1]==sign and   board[2][2]==sign:
        print(sign," is the winner ")
        #for columns 
        
    if board[0][0]==sign and  board[1][0]==sign and   board[2][0]==sign:
        print(sign," is the winner ")
    if board[0][1]==sign and  board[1][1]==sign and   board[1][2]==sign:
        print(sign," is the winner ")
    if board[0][2]==sign and  board[1][2]==sign and   board[2][2]==sign:
        print(sign," is the winner ")
        # for diagnols
    
    if board[0][0]==sign and  board[1][1]==sign and   board[2][2]==sign:
        print(sign," is the winner ")
    if board[0][2]==sign and  board[1][1]==sign and   board[2][0]==sign:
        print(sign," is the winner ")
        
        
def draw_move(board):
    comp_move=''
    comp_move==randrange(board)
    for row in range(3):
        for col in range(3):
            if board[row][col] in free_fields:
                comp_move=computer
            print(computer)
draw_move(board)    


user_move="O"
computer="X"
display_board(board)
victory_for(board, user_move)
victory_for(board, computer)