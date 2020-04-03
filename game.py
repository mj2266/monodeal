import os
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtCore import QEvent
from cardList import cardListWindow
current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir, "game.ui"))


color_to_rgb = {
    "sky_blue": (0, 191, 255),
    "red": (255, 0, 0),
    "blue": (0, 0, 102),
    "green": (0, 204, 0),
    "yellow": (255, 255, 0),
    "pink": (255, 0, 102),
    "utility": (204, 255, 153),
    "black": (255,255,255),
    "orange": (255, 102, 0),
}


class gameWindow(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)

        self.p1Property.clicked.connect(self.showCard)

    def showCard(self):
        self.cardPage = cardListWindow(parent= None, msg= "player X")
        self.cardPage.show()

    #     self.pushButton.installEventFilter(self)
    #     self.pushButton_2.installEventFilter(self)
    #
    # def eventFilter(self, obj, event):
    #
    #
    #
    #     if event.type() == QEvent.HoverEnter:
    #         if obj == self.pushButton:
    #             print("FOO")
    #
    #         if obj == self.pushButton_2:
    #             print("BOO")
    #         print("DOO")
    #     if event.type() == QEvent.HoverLeave:
    #         print("MOO")

        # return super(gameWindow, self).eventFilter(obj, event)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)

    w = gameWindow()
    w.show()
    sys.exit(app.exec_())


