import os
from PyQt5 import uic, QtWidgets, QtCore
from game import gameWindow

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir, "startWindow.ui"))


class startingWindow(Base, Form):
    def __init__(self, parent=None, msg="foo"):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        self.enterButton.clicked.connect(self.onclick)

    def showGameWindow(self, playername=""):
        print(playername)
        self.game = gameWindow(parent=None)
        self.game.show()

    def onclick(self):
        print("button is clicked")
        print(self.playerName.text())
        self.showGameWindow(playername=self.playerName.text())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)

    w = startingWindow()
    w.show()
    sys.exit(app.exec_())
