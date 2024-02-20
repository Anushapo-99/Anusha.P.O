

#TIC TAC TOE 
#------------


import random

def board_(board):
    for row in board:
        print("|".join(row))
    print("\n")

def winner(board, player):
    size = len(board)
   
    for i in range(size):
        if all(board[i][j] == player for j in range(size)) or all(board[j][i] == player for j in range(size)):
            return True
    if all(board[i][i] == player for i in range(size)) or all(board[i][size - 1 - i] == player for i in range(size)):
        return True
    return False

def board_full(board):
    size = len(board)
    return all(board[i][j] != ' ' for i in range(size) for j in range(size))

def get_available_moves(board):
    size = len(board)
    return [(i, j) for i in range(size) for j in range(size) if board[i][j] == ' ']

def computer_move(board):
    available_moves = get_available_moves(board)
    return random.choice(available_moves)

def main():
    size = 5
    board = [[' ' for _ in range(size)] for _ in range(size)]
    player = 'X'
    ai = 'O'

    while True:
        board_(board)

        if player == 'X':
            row = int(input(f"Enter the row (0 to {size-1}): "))
            col = int(input(f"Enter the column (0 to {size-1}): "))
            if 0 <= row < size and 0 <= col < size and board[row][col] == ' ':
                board[row][col] = player
            else:
                print("Invalid move. Try again.")
                continue
        else:
            move = computer_move(board)
            board[move[0]][move[1]] = ai

        if winner(board, player):
            board_(board)
            print(f"{player} wins!")
            break
        elif winner(board, ai):
            board_(board)
            print(f"{ai} wins!")
            break
        elif board_full(board):
            board_(board)
            print("It's a tie!")
            break

        player = 'O' if player == 'X' else 'X'

if __name__ == "__main__":
    main()
