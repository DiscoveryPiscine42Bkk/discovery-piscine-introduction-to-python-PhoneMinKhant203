from checkmate import is_attacked
import random

#Generate King's Position
def king_pos_generator():
    return random.randint(0,15)

def main():
    B_row = B_col = R_col = R_row = Q_row = Q_col = P_row = P_col = H_row = H_col = -1

    while 0 > B_row or B_row > 15: 
        B_row = int(input("Decide your B:Bishop row position from 0 to 15 ~ "))
    while 0 > B_col or B_col > 15:
        B_col = int(input("Decide your B:Bishop column position from 0 to 15 ~ "))

    
    while (0 > R_row or R_row > 15):
        R_row = int(input("Decide your R:Rook row position from 0 to 15 ~ "))
    while (0 > R_col or R_col > 15):
        R_col = int(input("Decide your R:Rook column position from 0 to 15 ~ "))
        

    while (0 > Q_row or Q_row > 15):
        Q_row = int(input("Decide your Q:Queen row position from 0 to 15 ~ "))
    while (0 > Q_col or Q_col > 15):
        Q_col = int(input("Decide your Q:Queen column position from 0 to 15 ~ "))


    while (0 > P_row or P_row > 15):
        P_row = int(input("Decide your P:Pawn row position from 0 to 15 ~ "))
    while (0 > P_col or P_col > 15):
        P_col = int(input("Decide your P:Pawn column position from 0 to 15 ~ "))


    while (0 > H_row or H_row > 15):
        H_row = int(input("Decide your H:Knight row position from 0 to 15 ~ "))
    while (0 > H_col or H_col > 15):
        H_col = int(input("Decide your H:Knight column position from 0 to 15 ~ "))

    chess_board = """\
................
................
................
................
................
................
................
................
................
................
................
................
................
................
................
................"""

    rows = chess_board.strip().split('\n')
    if not rows:
        print("Please Split the row with next line")

    num_rows = len(rows)

    board = [[c for c in row] for row in rows]
    
    board[B_row][B_col] = 'B'
    board[R_row][R_col] = 'R'
    board[P_row][P_col] = 'P'
    board[Q_row][Q_col] = 'Q'
    board[H_row][H_col] = 'H'
    #Generate King Position
    king_row, king_col = king_pos_generator(), king_pos_generator()

    while((king_row == B_row and king_col == B_col) and (king_row == R_row and king_col == R_col) and (king_row == P_row and king_col == P_col) and (king_row == Q_row and king_col == Q_col) and (king_row == H_row and king_col == H_col)):
        king_row = king_pos_generator()
        king_col = king_pos_generator()

    board[king_row][king_col] = 'K'

    for r in range(num_rows):
        for c in range(num_rows): 
            print(board[r][c], end="")
        print()

    is_attacked(board, king_row, king_col)

if __name__ == "__main__":
    main()
