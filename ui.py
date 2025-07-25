import tkinter as tk
from tkinter import messagebox
from logic import check_guess, color_guess_row
from wordlist import get_random_word

MAX_TRIES = 6
WORD_LENGTH = 5
target_word = get_random_word()

class WordleGame:
    """
    Κλάση για το γραφικό περιβάλλον του παιχνιδιού Wordle στα Ελληνικά.
    Διαχειρίζεται τη δημιουργία πλέγματος, την καταγραφή πληκτρολόγησης,
    και τον έλεγχο κάθε εικασίας.
    """
    def __init__(self, root):
        """
        Αρχικοποιεί το γραφικό περιβάλλον, τη λέξη-στόχο και τις βασικές μεταβλητές του παιχνιδιού.
        Args:
            root (tk.Tk): Το κύριο παράθυρο του Tkinter.
        """
        self.root = root
        self.root.title("Wordle στα Ελληνικά")
        self.tries = 0
        self.labels = []
        self.col = 0
        self.current_guess = [''] * WORD_LENGTH
        self.create_grid()

    def create_grid(self):
        """
        Δημιουργεί το πλέγμα με τις ετικέτες (labels) για την εμφάνιση γραμμάτων
        και συνδέει τα συμβάντα πληκτρολόγησης.
        """
        for row in range(MAX_TRIES):
            row_labels = []
            for col in range(WORD_LENGTH):
                lbl = tk.Label(self.root, text='', width=4, height=2, font=('Helvetica', 24), relief='solid', borderwidth=2, bg='white')
                lbl.grid(row=row, column=col, padx=5, pady=5)
                row_labels.append(lbl)
            self.labels.append(row_labels)

        self.root.bind("<Key>", self.handle_typing)
        self.root.bind("<Return>", self.check_current_guess)

    def handle_typing(self, event):
        """
        Διαχειρίζεται την πληκτρολόγηση χαρακτήρων από τον παίκτη.
        Args:
            event (tk.Event): Το συμβάν πληκτρολόγησης.
        """
        if self.tries >= MAX_TRIES:
            return

        if event.keysym == "BackSpace":
            if self.col > 0:
                self.col -= 1
                self.current_guess[self.col] = ''
                self.labels[self.tries][self.col].config(text='', bg='white')
            return

        if event.keysym == "Return":
            return

        ch = event.char.upper()
        if ch.isalpha() and len(ch) == 1:
            if self.col < WORD_LENGTH:
                self.current_guess[self.col] = ch
                self.labels[self.tries][self.col].config(text=ch.upper())
                self.col += 1

    def check_current_guess(self, event):
        """
        Ελέγχει την τρέχουσα λέξη-εικασία, εμφανίζει τα αποτελέσματα,
        και τερματίζει το παιχνίδι αν η λέξη βρεθεί ή εξαντληθούν οι προσπάθειες.
        Args:
            event (tk.Event): Το συμβάν πάτησης του πλήκτρου Enter.
        """
        if self.col < WORD_LENGTH:
            return

        guess = ''.join(self.current_guess)

        # if guess not in words:
        #    messagebox.showwarning("Άκυρη λέξη", "Η λέξη δεν υπάρχει.")
        #    for i in range(WORD_LENGTH):
        #        lbl = self.labels[self.tries][i]
        #        lbl.config(text='', bg='white', fg='black')
        #    self.col = 0
        #    self.current_guess = [''] * WORD_LENGTH
        #    return

        result = check_guess(guess, target_word)
        color_guess_row(self, self.tries, result)

        if guess == target_word:
            messagebox.showinfo("Μπράβο!", "Το βρήκες!")
            self.root.quit()
            return

        self.tries += 1
        self.col = 0
        self.current_guess = [''] * WORD_LENGTH

        if self.tries == MAX_TRIES:
            messagebox.showinfo("Τέλος παιχνιδιού", f"Η λέξη ήταν: {target_word}")
            self.root.quit()
            return