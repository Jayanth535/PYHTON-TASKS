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