from checkmate import checkmate
import sys

def main():
    n = len(sys.argv)
    if n < 2:
        print("None")
    else:
        for i in range(1, n):
            with open(sys.argv[i], "r") as file:
                board = file.read()
                print(board,'\n')
                checkmate(board)

if __name__ == "__main__":
    main()