# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/sender.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(403, 554)
        self.messageTextBox = QtWidgets.QTextEdit(Dialog)
        self.messageTextBox.setGeometry(QtCore.QRect(12, 38, 379, 81))
        self.messageTextBox.setObjectName("messageTextBox")
        self.sendButton = QtWidgets.QPushButton(Dialog)
        self.sendButton.setGeometry(QtCore.QRect(300, 141, 74, 32))
        self.sendButton.setObjectName("sendButton")
        self.cypherTextBrowser = QtWidgets.QTextBrowser(Dialog)
        self.cypherTextBrowser.setGeometry(QtCore.QRect(109, 191, 282, 81))
        self.cypherTextBrowser.setObjectName("cypherTextBrowser")
        self.capsuleLabel = QtWidgets.QLabel(Dialog)
        self.capsuleLabel.setGeometry(QtCore.QRect(10, 300, 74, 51))
        self.capsuleLabel.setWordWrap(True)
        self.capsuleLabel.setObjectName("capsuleLabel")
        self.cypherLabel = QtWidgets.QLabel(Dialog)
        self.cypherLabel.setGeometry(QtCore.QRect(10, 200, 81, 61))
        self.cypherLabel.setWordWrap(True)
        self.cypherLabel.setObjectName("cypherLabel")
        self.capsuleTextBrowser = QtWidgets.QTextBrowser(Dialog)
        self.capsuleTextBrowser.setGeometry(QtCore.QRect(110, 290, 282, 81))
        self.capsuleTextBrowser.setObjectName("capsuleTextBrowser")
        self.labelMessage = QtWidgets.QLabel(Dialog)
        self.labelMessage.setGeometry(QtCore.QRect(12, 12, 55, 16))
        self.labelMessage.setObjectName("labelMessage")
        self.delaySlider = QtWidgets.QSlider(Dialog)
        self.delaySlider.setGeometry(QtCore.QRect(106, 144, 171, 22))
        self.delaySlider.setMaximum(10)
        self.delaySlider.setSliderPosition(5)
        self.delaySlider.setOrientation(QtCore.Qt.Horizontal)
        self.delaySlider.setObjectName("delaySlider")
        self.delayLabel = QtWidgets.QLabel(Dialog)
        self.delayLabel.setGeometry(QtCore.QRect(12, 133, 35, 16))
        self.delayLabel.setObjectName("delayLabel")
        self.sliderLabel = QtWidgets.QLabel(Dialog)
        self.sliderLabel.setGeometry(QtCore.QRect(207, 161, 16, 16))
        self.sliderLabel.setText("")
        self.sliderLabel.setObjectName("sliderLabel")
        self.keyTextBrowser = QtWidgets.QTextBrowser(Dialog)
        self.keyTextBrowser.setGeometry(QtCore.QRect(110, 380, 282, 41))
        self.keyTextBrowser.setObjectName("keyTextBrowser")
        self.keyLabel = QtWidgets.QLabel(Dialog)
        self.keyLabel.setGeometry(QtCore.QRect(10, 390, 72, 16))
        self.keyLabel.setObjectName("keyLabel")
        self.trapdoortextBrowser = QtWidgets.QTextBrowser(Dialog)
        self.trapdoortextBrowser.setGeometry(QtCore.QRect(110, 490, 282, 51))
        self.trapdoortextBrowser.setObjectName("trapdoortextBrowser")
        self.trapdoorTextLabel = QtWidgets.QLabel(Dialog)
        self.trapdoorTextLabel.setGeometry(QtCore.QRect(10, 510, 101, 16))
        self.trapdoorTextLabel.setObjectName("trapdoorTextLabel")
        self.puzzleSolutionTextBrowser = QtWidgets.QTextBrowser(Dialog)
        self.puzzleSolutionTextBrowser.setGeometry(QtCore.QRect(110, 430, 282, 41))
        self.puzzleSolutionTextBrowser.setObjectName("puzzleSolutionTextBrowser")
        self.puzzleSolutionLabel = QtWidgets.QLabel(Dialog)
        self.puzzleSolutionLabel.setGeometry(QtCore.QRect(10, 430, 72, 41))
        self.puzzleSolutionLabel.setWordWrap(True)
        self.puzzleSolutionLabel.setObjectName("puzzleSolutionLabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sender"))
        self.sendButton.setText(_translate("Dialog", "Send"))
        self.capsuleLabel.setText(_translate("Dialog", "Encrypted key, Ck"))
        self.cypherLabel.setText(_translate("Dialog", "Encypted message, Cm"))
        self.labelMessage.setText(_translate("Dialog", "Message"))
        self.delayLabel.setText(_translate("Dialog", "Delay"))
        self.keyLabel.setText(_translate("Dialog", "Key, K"))
        self.trapdoorTextLabel.setText(_translate("Dialog", "Trapdoor, phi_n"))
        self.puzzleSolutionLabel.setText(_translate("Dialog", "Puzzle solution, b"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

