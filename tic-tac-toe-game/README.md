# Tic Tac Toe Game w/ AI Opponent

    # prompt 1: 

Write the python code to complete the following things

Create a functioning Tic Tac Toe game

Add an AI opponent for you to play against

Explain the code for the AI opponent to you. If the explanation is too complex, have it explain it to you in a way you can understand based on your knowledge level and experience.

    # GPT-4o Output:

Creating a Tic Tac Toe game with an AI opponent involves several steps. Here's a Python implementation using a simple AI opponent that uses the minimax algorithm, a common technique for building AI in turn-based games like Tic Tac Toe.

Let's start with the code:

```python

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
```

### Explanation of the AI Opponent (Minimax Algorithm)

The AI opponent uses the **minimax algorithm** to determine the best move. Here's a breakdown of how it works:

1. **Objective**: The minimax algorithm is designed to minimize the possible loss for a worst-case scenario. In Tic Tac Toe, the AI assumes that the opponent (you) will play optimally to minimize the AI's chances of winning.

2. **Recursive Function**: The `minimax` function is a recursive function that simulates all possible moves from a given board state and evaluates them based on the potential outcomes:
   - If the AI wins, it returns a score of `1`.
   - If the opponent wins, it returns a score of `-1`.
   - If the game is a draw, it returns a score of `0`.

3. **Maximizing and Minimizing**:
   - **Maximizing Player (AI)**: The AI tries to choose moves that maximize the score. It simulates all possible moves it can make and picks the one with the highest score.
   - **Minimizing Player (Human)**: The AI assumes the human will play optimally to minimize the AI's score. It simulates all possible moves the human can make and picks the one with the lowest score.

4. **Base Cases**:
   - The recursion stops if there's a winner or if the board is full, and the function returns the corresponding score.

5. **Best Move**:
   - The `find_best_move` function iterates over all available moves and uses the `minimax` function to find the move that results in the highest score for the AI.

### Simplified Explanation

Imagine playing Tic Tac Toe, where you think a few moves ahead and anticipate your opponent's moves to win. The AI does something similar:

- **Look Ahead**: The AI looks at all possible future game situations that could happen after each possible move.
- **Score Outcomes**: It gives scores to these possible future game situations: a high score if it wins, a low score if it loses, and a middle score for a draw.
- **Choose Wisely**: The AI chooses the move that leads to the highest score, assuming you will also try to block it from winning.

This process allows the AI to make strategic decisions and play optimally, making it challenging to beat.

If you have any questions about the code or need further explanation, feel free to ask!


    # time assignment 1 completed by Thomas Clark on 2024-08-08
