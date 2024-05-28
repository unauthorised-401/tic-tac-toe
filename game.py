import tkinter as tk
from tkinter import messagebox

player = 0  # 0 for player 1 (X), 1 for player 2 (O)
grid = [None for _ in range(9)]
buttons = []

def on_click(cell_number):
    """
    Handles the logic when a cell is clicked.

    Args:
        cell_number (int): The number of the clicked cell.

    Returns:
        None
    """
    global player, grid, buttons

    if grid[cell_number] is None:
        grid[cell_number] = player
        buttons[cell_number].config(text="X" if player == 0 else "O", bg="#F10E70" if player == 0 else "#3CC3B6")
        buttons[cell_number].config(state="disabled")
        
        winner = check_winner()
        if winner is not None:
            if winner == 0:
                messagebox.showinfo("Game Over", "Player 1 wins")
            elif winner == 1:
                messagebox.showinfo("Game Over", "Player 2 wins")
            elif winner == -1:
                messagebox.showinfo("Game Over", "It's a tie")
            root.destroy()
            return
        
        player = 1 - player  # switch player
        if player == 1:  # AI's turn
            best_move = move() 
            if best_move is not None:
                on_click(best_move)

def check_winner():
    """
    Check if there is a winner in the tic-tac-toe game.

    Returns:
        int or None: The player number (1 or 2) if there is a winner, -1 if it's a tie, or None if there is no winner yet.
    """
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for combination in winning_combinations:
        if grid[combination[0]] == grid[combination[1]] == grid[combination[2]] is not None:
            return grid[combination[0]]

    if not None in grid:
        return -1  # tie

    return None

def evaluate():
    """
    Evaluates the current state of the tic-tac-toe game.

    Returns:
        int: The evaluation score for the current state.
            - 30 if the player 1 (X) has won.
            - 0 if the game is a draw.
            - -30 if the player 2 (O) has won.
    """
    winner = check_winner()
    if winner == 0:
        return -30
    elif winner == 1:
        return 30
    elif winner == -1:
        return 0
    return 0

def minimax(grid, depth, is_maximizing):
    """
    Implements the minimax algorithm to determine the best move for the current player.

    Args:
        grid (list): The current state of the tic-tac-toe grid.
        depth (int): The current depth of the search tree.
        is_maximizing (bool): Indicates whether it's the maximizing player's turn.

    Returns:
        int: The score of the best move for the current player.

    """
    score = evaluate()
    if score != 0 or depth == 0:
        return score
    
    if not None in grid:
        return 0

    if is_maximizing:
        best_score = float("-inf")
        for i in range(9):
            if grid[i] is None:
                grid[i] = 1
                score = minimax(grid, depth - 1, False)
                grid[i] = None
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if grid[i] is None:
                grid[i] = 0
                score = minimax(grid, depth - 1, True)
                grid[i] = None
                best_score = min(score, best_score)
        return best_score

def move():
    """
    Determines the best move for the computer player in a Tic-Tac-Toe game.

    Returns:
        int: The index of the best move in the grid.
    """
    scores = []
    for i in range(9):
        score = float("-inf")
        if grid[i] is None:
            grid[i] = 1
            score = minimax(grid, 5, False)
            grid[i] = None
        scores.append(score)
    return scores.index(max(scores))

root = tk.Tk()
root.title("Tic Tac Toe")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - 500) // 2
y = (screen_height - 500) // 2
root.geometry(f"500x500+{x}+{y}")
root.resizable(0, 0)
root.configure(bg="#121212")
frame = tk.Frame(root, bg="#52DC23")
frame.pack(expand=True)

for i in range(9):
    btn = tk.Button(frame, font=("Helvetica", 20, "bold"), width=8, height=3, bg="white", command=lambda i=i: on_click(i))
    buttons.append(btn)
    btn.grid(row=i // 3, column=i % 3, padx=2, pady=2)

root.mainloop()
