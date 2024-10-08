import random

# Function to display the Tic Tac Toe board
def display_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

# Function to check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Check rows
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check columns
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):  # Check diagonals
        return True
    return False

# Function to check if the board is full
def is_full(board):
    return all([cell != ' ' for row in board for cell in row])

# Function to get available moves
def get_available_moves(board):
    moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return moves

# Minimax algorithm to determine the best move for AI
def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for move in get_available_moves(board):
            board[move[0]][move[1]] = 'O'
            score = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in get_available_moves(board):
            board[move[0]][move[1]] = 'X'
            score = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = ' '
            best_score = min(score, best_score)
        return best_score

# Function to find the best move for the AI
def find_best_move(board):
    best_score = float('-inf')
    best_move = None
    for move in get_available_moves(board):
        board[move[0]][move[1]] = 'O'
        score = minimax(board, 0, False)
        board[move[0]][move[1]] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

# Function to play the Tic Tac Toe game
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'  # Player starts first

    while True:
        display_board(board)

        if current_player == 'X':
            # Player's turn
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            if board[row][col] == ' ':
                board[row][col] = 'X'
                if check_winner(board, 'X'):
                    display_board(board)
                    print("You win!")
                    break
                current_player = 'O'
            else:
                print("Invalid move. Try again.")
        else:
            # AI's turn
            move = find_best_move(board)
            if move:
                board[move[0]][move[1]] = 'O'
                print(f"AI chooses position: {move}")
                if check_winner(board, 'O'):
                    display_board(board)
                    print("AI wins!")
                    break
                current_player = 'X'

        if is_full(board):
            display_board(board)
            print("It's a draw!")
            break

# Start the game
play_game()
