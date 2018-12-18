# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/receiver.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(622, 620)
        self.decryptedTrapTextBrowser = QtWidgets.QTextBrowser(Dialog)
        self.decryptedTrapTextBrowser.setGeometry(QtCore.QRect(330, 490, 271, 110))
        self.decryptedTrapTextBrowser.setObjectName("decryptedTrapTextBrowser")
        self.cypherTextBrowser = QtWidgets.QTextBrowser(Dialog)
        self.cypherTextBrowser.setGeometry(QtCore.QRect(130, 30, 280, 50))
        self.cypherTextBrowser.setObjectName("cypherTextBrowser")
        self.cypherLabel = QtWidgets.QLabel(Dialog)
        self.cypherLabel.setGeometry(QtCore.QRect(30, 30, 91, 51))
        self.cypherLabel.setWordWrap(True)
        self.cypherLabel.setObjectName("cypherLabel")
        self.capsuleLabel = QtWidgets.QLabel(Dialog)
        self.capsuleLabel.setGeometry(QtCore.QRect(30, 100, 81, 41))
        self.capsuleLabel.setWordWrap(True)
        self.capsuleLabel.setObjectName("capsuleLabel")
        self.capsuleTextBrowser = QtWidgets.QTextBrowser(Dialog)
        self.capsuleTextBrowser.setGeometry(QtCore.QRect(130, 100, 280, 50))
        self.capsuleTextBrowser.setObjectName("capsuleTextBrowser")
        self.timeTrapTextBrowser = QtWidgets.QTextBrowser(Dialog)
        self.timeTrapTextBrowser.setGeometry(QtCore.QRect(340, 410, 81, 25))
        self.timeTrapTextBrowser.setObjectName("timeTrapTextBrowser")
        self.timeTextBrowser = QtWidgets.QTextBrowser(Dialog)
        self.timeTextBrowser.setGeometry(QtCore.QRect(190, 410, 81, 25))
        self.timeTextBrowser.setObjectName("timeTextBrowser")
        self.timeLabel = QtWidgets.QLabel(Dialog)
        self.timeLabel.setGeometry(QtCore.QRect(250, 450, 123, 16))
        self.timeLabel.setObjectName("timeLabel")
        self.messageDecryptedLabel = QtWidgets.QLabel(Dialog)
        self.messageDecryptedLabel.setGeometry(QtCore.QRect(270, 380, 71, 16))
        self.messageDecryptedLabel.setObjectName("messageDecryptedLabel")
        self.decryptedTextBrowser = QtWidgets.QTextBrowser(Dialog)
        self.decryptedTextBrowser.setGeometry(QtCore.QRect(20, 490, 271, 110))
        self.decryptedTextBrowser.setObjectName("decryptedTextBrowser")
        self.puzzleSolutionLabel = QtWidgets.QLabel(Dialog)
        self.puzzleSolutionLabel.setGeometry(QtCore.QRect(250, 170, 101, 16))
        self.puzzleSolutionLabel.setObjectName("puzzleSolutionLabel")
        self.puzzleSolutionTextBrowser = QtWidgets.QTextBrowser(Dialog)
        self.puzzleSolutionTextBrowser.setGeometry(QtCore.QRect(10, 200, 271, 50))
        self.puzzleSolutionTextBrowser.setObjectName("puzzleSolutionTextBrowser")
        self.puzzleSolutionTrapTextBrowser = QtWidgets.QTextBrowser(Dialog)
        self.puzzleSolutionTrapTextBrowser.setGeometry(QtCore.QRect(320, 200, 271, 50))
        self.puzzleSolutionTrapTextBrowser.setObjectName("puzzleSolutionTrapTextBrowser")
        self.decryptedKeyLabel = QtWidgets.QLabel(Dialog)
        self.decryptedKeyLabel.setGeometry(QtCore.QRect(250, 270, 101, 16))
        self.decryptedKeyLabel.setObjectName("decryptedKeyLabel")
        self.decryptedKeyTrapTextBrowser = QtWidgets.QTextBrowser(Dialog)
        self.decryptedKeyTrapTextBrowser.setGeometry(QtCore.QRect(320, 310, 271, 50))
        self.decryptedKeyTrapTextBrowser.setObjectName("decryptedKeyTrapTextBrowser")
        self.decryptedKeyTextBrowser = QtWidgets.QTextBrowser(Dialog)
        self.decryptedKeyTextBrowser.setGeometry(QtCore.QRect(10, 310, 271, 50))
        self.decryptedKeyTextBrowser.setObjectName("decryptedKeyTextBrowser")
        self.trapdoorSolutionLabel = QtWidgets.QLabel(Dialog)
        self.trapdoorSolutionLabel.setGeometry(QtCore.QRect(410, 170, 111, 16))
        self.trapdoorSolutionLabel.setObjectName("trapdoorSolutionLabel")
        self.sequentialSolutionLabel = QtWidgets.QLabel(Dialog)
        self.sequentialSolutionLabel.setGeometry(QtCore.QRect(70, 170, 121, 16))
        self.sequentialSolutionLabel.setTextFormat(QtCore.Qt.AutoText)
        self.sequentialSolutionLabel.setObjectName("sequentialSolutionLabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Receiver"))
        self.cypherLabel.setText(_translate("Dialog", "Encrypted message, Cm"))
        self.capsuleLabel.setText(_translate("Dialog", "Encrypted key, Ck"))
        self.timeLabel.setText(_translate("Dialog", "Decrypted message"))
        self.messageDecryptedLabel.setText(_translate("Dialog", "Time, sec"))
        self.puzzleSolutionLabel.setText(_translate("Dialog", "Puzzle solution"))
        self.decryptedKeyLabel.setText(_translate("Dialog", "Decrypted key"))
        self.trapdoorSolutionLabel.setText(_translate("Dialog", "Trapdoor solution"))
        self.sequentialSolutionLabel.setText(_translate("Dialog", "Sequential solution"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

