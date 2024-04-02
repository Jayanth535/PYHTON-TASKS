from random import randrange
 
def display_board(board):
    print(' +-------+-------+-------+\n','|       |       |       |\n',
          '|   ' +board[0][0]+    '   |   ' +board[0][1] +   '   |   ' +board[0][2] +   '   |\n','|       |       |       |',)
    print(' +-------+-------+-------+\n','|       |       |       |\n',
          '|   ' +board[1][0]+    '   |   ' +board[1][1] +   '   |   ' +board[1][2] +   '   |\n','|       |       |       |',)
    print(' +-------+-------+-------+\n','|       |       |       |\n',
          '|   ' +board[2][0]+    '   |   ' +board[2][1] +   '   |   ' +board[2][2] +   '   |\n','|       |       |       |',)
    print(' +-------+-------+-------+')

def enter_move(board):
    board[1][1]="X"
    ok = False
    while not ok:
        move=input("enter your move:")
        ok=len(move)==1 and  move>="1" and move<="9"
        if not ok:
            print("bad input")
            continue
        move=int(move)-1
        row=move//3
        col=move%3
        sign=board[row][col]
        ok=sign not in ["X","O"] 
        if not ok:
            print(move ,"is already occupied repeat your input")
            continue
    board[row][col]="O" 
        
def make_list_of_free_fields(board):
    global free_fields
    free_fields=[]
    for row in range(3):
        for col in range(3):
            if board[row][col] !='O' and  board[row][col]!='X':
                free_fields.append([[row],[col]])
    return free_fields
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
    free=make_list_of_free_fields(board)
    counter=len(free)
    print(counter)
    if counter > 0:
        it=randrange(counter)
        row,col=free[it]
        board[row][col]= "X"
        print(row,col)
board=[ [3 * j + i + 1 for i in range(3)] for j in range(3)]
draw_move(board)
