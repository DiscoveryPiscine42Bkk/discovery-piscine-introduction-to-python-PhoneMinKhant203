
def checkmate(board_string):

    if not board_string:
        print("Fail")
        
    rows = board_string.strip().split('\n')
    if not rows:
        print("Please Split the row with next line")

    num_rows = len(rows)

    # Check for consistent row lengths and ensure the board is square
    row_lengths = [len(row) for row in rows]
    if not all(length == num_rows for length in row_lengths):
        print("The board is not square")
        return

    #board = [[c if c in 'KPRBQH' else '.' for c in row] for row in rows]
    board = [[c for c in row] for row in rows]
    
    king_row, king_col = -1, -1
    # Find the King's position
    for r in range(num_rows): 
        for c in range(num_rows): 
            if board[r][c] == 'K':
                king_row, king_col = r, c
                break

    if king_row == -1 or king_col == -1:
        print("King is not Found")  # King not found

    # Check for attacks from each type of piece
    is_attacked(board, king_row, king_col)

def is_attacked(board, king_row, king_col):
    num_rows = len(board)

    if checkDiagonalsAndLines(king_row, king_col, board, 'B', [(1, 1), (1, -1), (-1, 1), (-1, -1)]):
        print("Success \n")
        return

    elif checkDiagonalsAndLines(king_row, king_col, board, 'R', [(0, 1), (0, -1), (1, 0), (-1, 0)]):
        print("Success \n")
        return

    elif checkDiagonalsAndLines(king_row, king_col, board, 'Q', [(1, 1), (1, -1), (-1, 1), (-1, -1)]) or checkDiagonalsAndLines(king_row, king_col, board, 'Q', [(0, 1), (0, -1), (1, 0), (-1, 0)]):
        print("Success \n")
        return
    
    elif 0 <= king_row < num_rows - 1 and 0 <= king_col < num_rows - 1:
        if board[king_row + 1][king_col - 1] == 'P' or board[king_row + 1][king_col + 1] == 'P':
            print("Success \n")
            return
        #For Bonus Part
        elif board[king_row + 2][king_col - 1] == 'H' or board[king_row + 2][king_col + 1] == 'H' or board[king_row - 2][king_col - 1] == 'H' or board[king_row - 2][king_col + 1] == 'H' or board[king_row - 1][king_col + 2] == 'H' or board[king_row - 1][king_col - 2] == 'H' or board[king_row + 1][king_col + 2] == 'H' or board[king_row + 1][king_col - 2] == 'H':
            print("Success \n")
            return
        
    print("Fail \n")  # King is not in check

def checkDiagonalsAndLines(king_row, king_col, board, attack_piece, dir_list):
    num_rows = len(board)
    for row_dir, col_dir in dir_list:
        r, c = king_row + row_dir, king_col + col_dir
        while 0 <= r < num_rows and 0 <= c < num_rows:
            if board[r][c] == attack_piece:
                return True     
            r += row_dir
            c += col_dir
    return False