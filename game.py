import tkinter as tk
from tkinter import messagebox

player = 0 # 0 for player 1, 1 for player 2
grid = [None for _ in range(9)]
buttons = []
def on_click(cell_number):
    global player
    global grid
    global buttons
    grid[cell_number] = player
    buttons[cell_number].config(text="X" if player == 0 else "O",bg = "#F10E70" if player == 0 else "#3CC3B6") 
    buttons[cell_number].config(state="disabled")
    player = not player  
    winner = check_winner(grid)
    if winner == 0:
        messagebox.showinfo("Game Over", "Player 1 wins")
        root.destroy()
    elif winner == 1:
        messagebox.showinfo("Game Over", "Player 2 wins")
        root.destroy()
    elif winner == -1:
        messagebox.showinfo("Game Over", "It's a tie")
        root.destroy()

def check_winner(grid):
    winning_combinations = [[0,1,2],[3,4,5],[6,7,8],
                            [0,3,6],[1,4,7],[2,5,8],
                            [0,4,8],[2,4,6]]

    for combination in winning_combinations:
        if grid[combination[0]] == grid[combination[1]] == grid[combination[2]] == 0:
            return 0
        elif grid[combination[0]] == grid[combination[1]] == grid[combination[2]] == 1:
            return 1
    if not None in grid:
        return -1
    return None
    

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
    btn = tk.Button(frame,font=("Helvetica", 20,"bold"), width=8, height=3,bg="white",command=lambda i=i :on_click(i))
    buttons.append(btn)
    btn.grid(row=i // 3, column=i % 3,padx=2, pady=2)
  
root.mainloop()

