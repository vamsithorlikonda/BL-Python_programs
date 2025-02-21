import random

# Initialize 3x3 board with empty spaces
board = [[' ' for _ in range(3)] for _ in range(3)]

def print_board():
    """Prints the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(symbol):
    """Checks if the given symbol ('X' or 'O') has won."""
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)) or all(board[j][i] == symbol for j in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2 - i] == symbol for i in range(3)):
        return True
    
    return False

def is_draw():
    """Checks if the board is full (game is a draw)."""
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def player_move():
    """Takes user input and marks 'X' in the chosen cell."""
    while True:
        try:
            row, col = map(int, input("Enter row and column (1-3 1-3) separated by space: ").split())
            if 1 <= row <= 3 and 1 <= col <= 3 and board[row - 1][col - 1] == ' ':
                board[row - 1][col - 1] = 'X'
                break
            else:
                print("Invalid move! Cell is occupied or out of range. Try again.")
        except ValueError:
            print("Invalid input! Enter numbers between 1-3.")

def computer_move():
    """Computer picks a random empty cell and marks 'O'."""
    while True:
        row, col = random.randint(0, 2), random.randint(0, 2)
        if board[row][col] == ' ':
            board[row][col] = 'O'
            print(f"Computer placed 'O' at ({row+1}, {col+1})")
            break

# Main game loop
print("Welcome to Tic-Tac-Toe! You are 'X' and the computer is 'O'.")
print_board()

while True:
    # Player move
    player_move()
    print_board()
    if check_winner('X'):
        print("Congratulations! You win!")
        break
    if is_draw():
        print("It's a draw!")
        break

    # Computer move
    computer_move()
    print_board()
    if check_winner('O'):
        print("Computer wins! Better luck next time.")
        break
    if is_draw():
        print("It's a draw!")
        break
