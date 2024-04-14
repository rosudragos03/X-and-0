import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel

class TicTacToeGame(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Tic Tac Toe")
        self.setGeometry(100, 100, 300, 300)

        self.board = [' '] * 9
        self.current_player = 'X'
        self.buttons = []

        for i in range(9):
            button = QPushButton('', self)
            button.setFont(button.font())
            button.clicked.connect(lambda _, i=i: self.make_move(i))
            self.buttons.append(button)

        self.reset_button = QPushButton('Reset', self)
        self.reset_button.clicked.connect(self.reset_game)

        layout = QVBoxLayout()
        grid_layout = [self.buttons[i:i+3] for i in range(0, 9, 3)]

        for row in grid_layout:
            row_layout = QHBoxLayout()
            for button in row:
                row_layout.addWidget(button)
            layout.addLayout(row_layout)

        layout.addWidget(self.reset_button)
        self.setLayout(layout)

        self.update_ui()

    def make_move(self, index):
        if self.board[index] == ' ':
            self.board[index] = self.current_player
            self.update_ui()
            winner = self.check_winner()
            if winner:
                self.show_winner(winner)
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def update_ui(self):
        for i in range(9):
            self.buttons[i].setText(self.board[i])

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return self.board[combo[0]]
        if ' ' not in self.board:
            return 'Tie'
        return None

    def show_winner(self, winner):
        message = f'Winner: {winner}' if winner != 'Tie' else 'It\'s a Tie!'
        winner_label = QLabel(message, self)
        winner_label.setAlignment(QtCore.Qt.AlignCenter)
        winner_label.setFont(winner_label.font())
        self.layout().addWidget(winner_label)

    def reset_game(self):
        self.board = [' '] * 9
        self.current_player = 'X'
        self.update_ui()
        winner_label = self.findChild(QLabel)
        if winner_label:
            winner_label.deleteLater()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TicTacToeGame()
    ex.show()
    sys.exit(app.exec_())
