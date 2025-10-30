import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe 🎮")
        self.root.configure(bg="#2b2b2b")
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        self.create_ui()

    def create_ui(self):
        title = tk.Label(self.root, text="Tic Tac Toe", font=("Arial", 24, "bold"),
                         bg="#2b2b2b", fg="#00ffcc", pady=20)
        title.pack()

        frame = tk.Frame(self.root, bg="#2b2b2b")
        frame.pack()

        for i in range(9):
            btn = tk.Button(
                frame, text="", font=("Arial", 20, "bold"),
                width=5, height=2, bg="#333333", fg="#ffffff",
                command=lambda i=i: self.on_click(i)
            )
            btn.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(btn)

        reset_btn = tk.Button(
            self.root, text="Restart 🔄", font=("Arial", 14, "bold"),
            bg="#00ffcc", fg="#2b2b2b", width=10, command=self.reset_game
        )
        reset_btn.pack(pady=15)

    def on_click(self, i):
        if self.board[i] == "" and not self.check_winner():
            self.board[i] = self.current_player
            self.buttons[i].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"🎉 Player {self.current_player} wins!")
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
            (0, 4, 8), (2, 4, 6)              # diagonals
        ]
        for a, b, c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] != "":
                for idx in (a, b, c):
                    self.buttons[idx].config(bg="#00ffcc", fg="#2b2b2b")
                return True
        return False

    def reset_game(self):
        self.current_player = "X"
        self.board = [""] * 9
        for btn in self.buttons:
            btn.config(text="", bg="#333333", fg="#ffffff")

if __name__ == "__main__":
    root = tk.Tk()
    TicTacToe(root)
    root.mainloop()
