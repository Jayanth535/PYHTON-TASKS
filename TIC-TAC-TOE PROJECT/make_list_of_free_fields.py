def make_list_of_free_fields(board):
    global free_fields
    free_fields=[]
    for row in range(3):
        for col in range(3):
            if board[row][col] !='O' and  board[row][col]!='X':
                free_fields.append([[row],[col]])
board=[['1','2','3'],['4','X','6'],['7','8','9']]
make_list_of_free_fields(board)