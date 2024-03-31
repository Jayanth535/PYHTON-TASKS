def display_board(board):
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' +board[0][0]+    '   |   ' +board[0][1] +   '   |   ' +board[0][2] +   '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' +board[1][0]+    '   |   ' +board[1][1] +   '   |   ' +board[1][2] +   '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' +board[2][0]+    '   |   ' +board[2][1] +   '   |   ' +board[2][2] +   '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
board=[['1','2','3'],['4','5','6'],['7','8','9']]
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
    free_fields=[]
    for row in range(3):
        for col in range(3):
            if board[row][col] !='O' and  board[row][col]!='X':
                free_fields.append([[row],[col]])
    print(free_fields)
make_list_of_free_fields(board)
# def victory_for(board, sign):
#     # The function analyzes the board's status in order to check if 
#     # the player using 'O's or 'X's has won the game

# def draw_move(board):
#     # The function draws the computer's move and updates the board.
