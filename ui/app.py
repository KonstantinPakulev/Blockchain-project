import ui.sender as sender
import ui.receiver as receiver
import sys
import time
from cipher.utils import *
from PyQt5 import QtWidgets
from puzzle.puzzle import TimeLockPuzzle
from threading import Thread


class SenderApp(QtWidgets.QMainWindow, sender.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.sendButton.clicked.connect(self.send_message)
        self.sliderLabel.setText(str(self.delaySlider.value()))
        self.delaySlider.valueChanged.connect(self.update_slider_label)

        self.time_lock_puzzle = TimeLockPuzzle()

    def send_message(self):
        self.time_lock_puzzle.T = self.delaySlider.value()
        message = self.messageTextBox.toPlainText()

        n, a, t, Ck, Cm, K, b, phi_n = self.time_lock_puzzle.generate_puzzle(message)

        self.cypherTextBrowser.setPlainText(str(Cm))
        self.capsuleTextBrowser.setPlainText(str(Ck))
        self.keyTextBrowser.setPlainText(binary_to_acsii(bin(K)[2:].zfill(168)))
        self.puzzleSolutionTextBrowser.setPlainText(str(b))
        self.trapdoortextBrowser.setPlainText(str(phi_n))

        self.receiver.receive_message(n, a, t, Ck, Cm, phi_n)

    def update_slider_label(self):
        self.sliderLabel.setText(str(self.delaySlider.value()))


class ReceiverApp(QtWidgets.QMainWindow, receiver.Ui_Dialog):
    def __init__(self, time_lock_puzzle):
        super().__init__()
        self.setupUi(self)
        self.time_lock_puzzle = time_lock_puzzle

    def receive_message(self, n, a, t, Ck, Cm, phi_n):
        self.cypherTextBrowser.setPlainText(str(Cm))
        self.capsuleTextBrowser.setPlainText(str(Ck))

        start_time = time.time()
        solution, K, message = self.time_lock_puzzle.solve_puzzle(n, a, t, Ck, Cm)
        elapsed_time = time.time() - start_time

        self.puzzleSolutionTextBrowser.setPlainText(str(solution))
        self.decryptedKeyTextBrowser.setPlainText(str(K))
        self.timeTextBrowser.setPlainText('{0:.3f}'.format(elapsed_time))
        self.decryptedTextBrowser.setPlainText(str(message[1]))

        start_time = time.time()
        solution_trap, K_trap, message_trap = self.time_lock_puzzle.solve_puzzle_via_trapdoor(n, a, t, Ck, Cm, phi_n)
        elapsed_time = time.time() - start_time

        self.puzzleSolutionTrapTextBrowser.setPlainText(str(solution_trap))
        self.decryptedKeyTrapTextBrowser.setPlainText(str(K_trap))
        self.timeTrapTextBrowser.setPlainText('{0:.3f}'.format(elapsed_time))
        self.decryptedTrapTextBrowser.setPlainText(str(message_trap[1]))


def main():
    app = QtWidgets.QApplication(sys.argv)  
    sender_window = SenderApp()
    sender_window.show()

    receiver_window = ReceiverApp(sender_window.time_lock_puzzle)
    sender_window.receiver = receiver_window
    receiver_window.show()
    app.exec_()


if __name__ == '__main__':
    main()
