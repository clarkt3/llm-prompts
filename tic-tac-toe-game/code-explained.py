# the code is explained line by line for each statment below
    # added this for clearity

import random  # Import the random module (though it's not used in this code)

# Function to display the Tic Tac Toe board
def display_board(board):
    for row in board:
        print(' | '.join(row))  # Print each row with cells separated by '|'
        print('-' * 9)  # Print a separator line after each row

# Function to check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Check if all cells in a row are the same player
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check if all cells in a column are the same player
            return True
    # Check both diagonals
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False  # Return False if no win condition is met

# Function to check if the board is full
def is_full(board):
    # Check if all cells are filled
    return all([cell != ' ' for row in board for cell in row])

# Function to get available moves
def get_available_moves(board):
    # Generate a list of empty positions (available moves)
    moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return moves

# Minimax algorithm to determine the best move for AI
def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):  # If AI wins, return score of 1
        return 1
    if check_winner(board, 'X'):  # If player wins, return score of -1
        return -1
    if is_full(board):  # If the board is full and there's no winner, it's a draw
        return 0

    if is_maximizing:
        best_score = float('-inf')  # Initialize best score for maximizing player
        for move in get_available_moves(board):  # Iterate through available moves
            board[move[0]][move[1]] = 'O'  # Try a move for AI
            score = minimax(board, depth + 1, False)  # Recursively call minimax for the opponent
            board[move[0]][move[1]] = ' '  # Undo the move
            best_score = max(score, best_score)  # Choose the maximum score
        return best_score
    else:
        best_score = float('inf')  # Initialize best score for minimizing player
        for move in get_available_moves(board):  # Iterate through available moves
            board[move[0]][move[1]] = 'X'  # Try a move for the player
            score = minimax(board, depth + 1, True)  # Recursively call minimax for the AI
            board[move[0]][move[1]] = ' '  # Undo the move
            best_score = min(score, best_score)  # Choose the minimum score
        return best_score

# Function to find the best move for the AI
def find_best_move(board):
    best_score = float('-inf')  # Initialize the best score
    best_move = None  # Initialize the best move
    for move in get_available_moves(board):  # Iterate through available moves
        board[move[0]][move[1]] = 'O'  # Try a move for AI
        score = minimax(board, 0, False)  # Calculate the minimax score
        board[move[0]][move[1]] = ' '  # Undo the move
        if score > best_score:  # If the score is better, update the best score and move
            best_score = score
            best_move = move
    return best_move  # Return the best move found

# Function to play the Tic Tac Toe game
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]  # Initialize the 3x3 board with empty spaces
    current_player = 'X'  # Player starts first

    while True:  # Main game loop
        display_board(board)  # Display the current state of the board

        if current_player == 'X':  # Player's turn
            # Get the player's move
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            if board[row][col] == ' ':  # Check if the move is valid
                board[row][col] = 'X'  # Place the player's mark on the board
                if check_winner(board, 'X'):  # Check if the player wins
                    display_board(board)
                    print("You win!")
                    break
                current_player = 'O'  # Switch to AI's turn
            else:
                print("Invalid move. Try again.")  # Invalid move, prompt to try again
        else:
            # AI's turn
            move = find_best_move(board)  # Determine the best move for AI
            if move:
                board[move[0]][move[1]] = 'O'  # Place the AI's mark on the board
                print(f"AI chooses position: {move}")
                if check_winner(board, 'O'):  # Check if the AI wins
                    display_board(board)
                    print("AI wins!")
                    break
                current_player = 'X'  # Switch to player's turn

        if is_full(board):  # Check if the board is full
            display_board(board)
            print("It's a draw!")  # If full, the game is a draw
            break

# Start the game
play_game()  # Call the function to start the game
