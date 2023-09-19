# Tic-Tac-Toe with MINMAX algorithm
# Authors: Rashawn Hill
# Date: 09/17/2023
# Assignment Number: #1

# Function to display the Tic-Tac-Toe board
def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")


# Function to check for a winner
def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]  # diagonals
    ]

    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != " ":
            return board[combination[0]]
    return None


# Function to check for a tie
def check_tie(board):
    return " " not in board


# Function to implement the MINMAX algorithm
def minmax(board, depth, maximizing):
    winner = check_winner(board)
    if winner == 'X':
        return -10 + depth
    elif winner == 'O':
        return 10 - depth
    elif check_tie(board):
        return 0

    if maximizing:
        max_eval = float('-inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = 'O'
                eval = minmax(board, depth + 1, False)
                board[i] = " "
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = 'X'
                eval = minmax(board, depth + 1, True)
                board[i] = " "
                min_eval = min(min_eval, eval)
        return min_eval


# Function for the player's move
def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = 'X'
                break
            else:
                print("Cell already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Try again.")


# Function for the computer's move
def computer_move(board):
    max_eval = float('-inf')
    best_move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = 'O'
            eval = minmax(board, 0, False)
            board[i] = " "
            if eval > max_eval:
                max_eval = eval
                best_move = i
    board[best_move] = 'O'


# Main Program
if __name__ == "__main__":
    print(
        "Welcome to Tic-Tac-Toe with AI! This app allows you to play Tic-Tac-Toe against a computer using the MINMAX algorithm.")

    while True:
        board = [" " for _ in range(9)]
        while True:
            display_board(board)
            player_move(board)

            winner = check_winner(board)
            if winner:
                print(f"{winner} wins!")
                break
            elif check_tie(board):
                print("It's a tie!")
                break

            computer_move(board)

            winner = check_winner(board)
            if winner:
                print(f"{winner} wins!")
                break
            elif check_tie(board):
                print("It's a tie!")
                break

        replay = input("Do you want to play again? (y/n): ")
        if replay.lower() != 'y':
            break