import os
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtCore import QEvent
from cardList import cardListWindow
current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir, "game.ui"))


color_to_rgb = {
    "sky_blue": "rgb(0, 191, 255)",
    "red": "rgb(255, 0, 0)",
    "blue": "rgb(0, 0, 102)",
    "green": "rgb(0, 204, 0)",
    "yellow": "rgb(255, 255, 0)",
    "pink": "rgb(255, 0, 102)",
    "utility": "rgb(204, 255, 153)",
    "black": "rgb(255,255,255)",
    "orange": "rgb(255, 102, 0)",
}


class gameWindow(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)

        self.p1Property.clicked.connect(self.showCard)

        self.button = QtWidgets.QPushButton("Bangladesh",self.frame)
        self.button2 = QtWidgets.QPushButton("Pakistan",self.frame)
        self.button.setGeometry( 0,0,100,40)
        self.button2.setGeometry( 150,0,100,40)

        self.button.setStyleSheet("background-color:"+color_to_rgb["pink"])
        self.button2.setStyleSheet("background-color:"+color_to_rgb["green"])


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


