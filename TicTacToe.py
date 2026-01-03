import numpy as np

matrix = np.array([
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
])

# Check valid moves
def board(r, c, symbol, matrix):
    if r > 2 or c > 2 or r < 0 or c < 0:
        print("INVALID ENTRY! Indices must be (0,1,2)")
        return False
    elif matrix[r, c] != ' ':
        print("Space already occupied! Enter indices again.", end="\n\n")
        return False
    else:
        matrix[r, c] = symbol
        print(matrix)
        return True

# Making move on the board
def move(symbol):
    print(symbol, "'s TURN")
    while True:
        try:
            r1 = int(input("Enter the row index (0,1,2): "))
            c1 = int(input("Enter the column index (0,1,2): "))
            if board(r1, c1, symbol, matrix):
                break
        except ValueError:
            print("INVALID ENTRY! Please enter numbers only (0,1,2).")

# Check for winner 
def winner(matrix):
    # Check rows
    for i in range(3):
        if matrix[i, 0] == matrix[i, 1] == matrix[i, 2] and matrix[i, 0] != ' ':
            print(f"\nThe winner is {matrix[i, 0]}!")
            return False

    # Check columns
    for col in range(3):
        if matrix[0, col] == matrix[1, col] == matrix[2, col] and matrix[0, col] != ' ':
            print(f"\nThe winner is {matrix[0, col]}!")
            return False

    # Check diagonals
    if matrix[0, 0] == matrix[1, 1] == matrix[2, 2] and matrix[0, 0] != ' ':
        print(f"\nThe winner is {matrix[0, 0]}!")
        return False
    if matrix[0, 2] == matrix[1, 1] == matrix[2, 0] and matrix[0, 2] != ' ':
        print(f"\nThe winner is {matrix[0, 2]}!")
        return False

    # Check for draw (no empty spaces left)
    if ' ' not in matrix:
        print("\nIt's a draw!")
        return False

    # No winner yet
    return True

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("Player 1: X")
    print("Player 2: O\n")
    print("Empty board:")
    print(matrix)
    
    while True:
        move('X')
        if not winner(matrix):
            break
            
        move('O')
        if not winner(matrix):
            break


if __name__ == "__main__":
    play_game()