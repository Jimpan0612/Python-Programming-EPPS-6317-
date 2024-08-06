#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""6317 Lab7 Create a Guessing Game Application

In this exercise, you will create a guessing game application using PyQt5. 
The game will pick a random number and allow players to guess the number. 
You'll also create a hint button to give players some clues about the correct number.

References
Chat GPT

Created on Tue Oct 10 22:03:54 2023

@author: jimpan
"""

from PyQt5.QtWidgets import *
import random
import sys

from frmGuess import Ui_frmGuess

# Global variables to store random number and times guessed
times_guessed = 0
num_to_guess = random.randrange(1, 101)
hint = None

# Create Main Window
class Mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frmGuess()
        # Call UI set up in QtDesigner/pyuic5
        self.ui.setupUi(self)
        # Reset times guessed label
        self.update_times_guessed_label()  # Initial setup
        # Connect Guess button to guess_click function
        self.ui.guess_button.clicked.connect(self.guess_click)
        self.ui.hint_button.clicked.connect(self.hint_click)
        # Show form
        self.show()
        
    def update_times_guessed_label(self):
        self.ui.timesGuessedLabel.setText(str(times_guessed))

    def guess_click(self):
        global num_to_guess
        global times_guessed 
        
        guess, okPressed = QInputDialog.getInt(self, "Enter Guess", "Guess 1-100", 1, 1, 100, 1)
        if okPressed:
            times_guessed = times_guessed + 1
            self.update_times_guessed_label()  # Update the label
            if guess == num_to_guess:
                QMessageBox.question(self, "Congratulations", "You guessed the right number in " +
                                     str(times_guessed), QMessageBox.Ok)
                # Reset number to guess
                num_to_guess = random.randrange(1, 101)
                # Reset times guessed
                times_guessed = 0
                # Reset label to 0
                self.update_times_guessed_label()  # Update the label again
                # Reset the hint
                global hint
                hint = None

            elif guess < num_to_guess:
                QMessageBox.question(self, "Low", "Your guess is too low.", QMessageBox.Ok)
            elif guess > num_to_guess:
                QMessageBox.question(self, "High", "Your guess is too high.", QMessageBox.Ok)

    def hint_click(self):
        global hint
        if hint is None:
            hint = random.randint(-5, 5)
        hint_number = num_to_guess + hint
        QMessageBox.information(self, "Hint", f"The hint is within {hint_number}", QMessageBox.Ok)
        # Add a penalty of 5 to the total number of guesses
        global times_guessed
        times_guessed += 5
        self.update_times_guessed_label()  # Update the label to reflect the penalty

# Run the main function
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Mainwindow()
    sys.exit(app.exec())


