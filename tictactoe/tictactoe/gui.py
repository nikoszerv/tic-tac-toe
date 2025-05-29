# gui.py

import tkinter as tk
from tkinter import messagebox
from game_logic import Game


class TicTacToeGUI:
    def __init__(self, root, game_logic):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.game = Game()
        self.time_left = 10
        self.timer_id = None
        self.timer_running = False

        self.buttons = []
        for i in range(9):
            button = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                               command=lambda index=i: self.button_click(index))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

        self.score_label = tk.Label(root, text="", font=("Arial", 14))
        self.score_label.grid(row=3, column=0, columnspan=3)

        self.timer_label = tk.Label(root, text="", font=("Arial", 14))
        self.timer_label.grid(row=4, column=0, columnspan=3)

        
        self.bottom_frame = tk.Frame(root)
        self.bottom_frame.grid(row=5, column=0, columnspan=3, sticky='we')

        self.reset_button = tk.Button(self.bottom_frame, text="Reset", command=self.reset_board)
        self.reset_button.pack(side='left', padx=10, pady=10)

        self.update_scoreboard()
        self.reset_timer()

    def button_click(self, index):
        player = self.game.current_player
        if self.game.make_move(index):
            self.buttons[index].config(text=player)

            winner = self.game.check_winner()
            if winner:
                self.handle_win(winner)
                return

            if self.game.is_draw():
                self.handle_draw()
                return

            self.game.switch_player()
            self.reset_timer()

            if self.game.current_player == "O":
                self.root.after(500, self.ai_play)

    def ai_play(self):
        index = self.game.ai_move()
        if index is not None and self.game.make_move(index):
            self.buttons[index].config(text = "O")
            winner = self.game.check_winner()
            if winner:
                self.handle_win(winner)
                return
            elif self.game.is_draw():
                self.handle_draw()
                return
            self.game.switch_player()
            self.reset_timer()

    def handle_win(self, winner):
        self.stop_timer()
        if winner == "X":
            self.game.score_X += 1
        else:
            self.game.score_O += 1
        self.update_scoreboard()
        messagebox.showinfo("Game Over", f"Player {winner} wins!")
        self.reset_board()

    def handle_draw(self):
        self.stop_timer()
        messagebox.showinfo("Game Over", "It's a draw!")
        self.reset_board()

    def reset_board(self):
        self.game.reset_board()
        for button in self.buttons:
            button.config(text=" ")
        self.stop_timer()
        self.reset_timer()

    def update_scoreboard(self):
        x_score = self.game.score_X
        o_score = self.game.score_O
        self.score_label.config(text=f"X: {x_score} | O: {o_score}")

    def countdown(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time left: {self.time_left}")
            self.timer_id = self.root.after(1000, self.countdown)
        else:
            messagebox.showinfo("Time's up!", f"Player {self.game.current_player} ran out of time!")
            self.game.switch_player()
            self.reset_board()

    def reset_timer(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        self.time_left = 10
        self.timer_label.config(text=f"Time left: {self.time_left}")
        self.timer_id = self.root.after(1000, self.countdown)

    def stop_timer(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None
