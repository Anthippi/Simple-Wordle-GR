import tkinter as tk
from ui import WordleGame

if __name__ == "__main__":
    # Δημιουργία κύριου παραθύρου και εκκίνηση του παιχνιδιού
    root = tk.Tk()
    game = WordleGame(root)
    root.mainloop()
