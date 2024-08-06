# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lab7.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmGuess(object):
    def setupUi(self, frmGuess):
        frmGuess.setObjectName("frmGuess")
        frmGuess.resize(454, 159)
        self.guess_button = QtWidgets.QPushButton(frmGuess)
        self.guess_button.setGeometry(QtCore.QRect(50, 30, 113, 32))
        self.guess_button.setObjectName("guess_button")
        self.hint_button = QtWidgets.QPushButton(frmGuess)
        self.hint_button.setGeometry(QtCore.QRect(252, 30, 131, 32))
        self.hint_button.setObjectName("hint_button")
        self.guessTextLabel = QtWidgets.QLabel(frmGuess)
        self.guessTextLabel.setGeometry(QtCore.QRect(50, 90, 121, 20))
        self.guessTextLabel.setObjectName("guessTextLabel")
        self.timesGuessedLabel = QtWidgets.QLabel(frmGuess)
        self.timesGuessedLabel.setGeometry(QtCore.QRect(240, 90, 60, 16))
        self.timesGuessedLabel.setText("")
        self.timesGuessedLabel.setObjectName("timesGuessedLabel")

        self.retranslateUi(frmGuess)
        QtCore.QMetaObject.connectSlotsByName(frmGuess)

    def retranslateUi(self, frmGuess):
        _translate = QtCore.QCoreApplication.translate
        frmGuess.setWindowTitle(_translate("frmGuess", "Guess a number between 1 and 100"))
        self.guess_button.setText(_translate("frmGuess", "Guess..."))
        self.hint_button.setText(_translate("frmGuess", "Give me a hint..."))
        self.guessTextLabel.setText(_translate("frmGuess", "Number of guess:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmGuess = QtWidgets.QDialog()
    ui = Ui_frmGuess()
    ui.setupUi(frmGuess)
    frmGuess.show()
    sys.exit(app.exec_())

