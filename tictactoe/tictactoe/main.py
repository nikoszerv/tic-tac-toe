# main.py

import tkinter as tk
from gui import TicTacToeGUI
from game_logic import Game
from scoreboard import Scoreboard

if __name__ == "__main__":
    window = tk.Tk()
    window.title("TicTacToe")
    game_logic = Game()
    gui = TicTacToeGUI(window, game_logic)
    window.mainloop()